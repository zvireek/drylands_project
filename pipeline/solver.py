import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

# Defining derivative matrices
"""def D1_left(N):
  D1 = np.eye(N, k=1) - np.eye(N)
  return D1
def D1_right(N):
  D1 = -np.eye(N, k=-1) + np.eye(N)
  return D1"""

def D2(N):
  D2_matr = -2 * np.eye(N) + np.eye(N, k=1) + np.eye(N, k=-1)
  return D2_matr

def D2_sparse(N):
    main_diag = -2 * np.ones(N)
    side_diag = np.ones(N - 1)
    D2_1d = sp.diags([side_diag, main_diag, side_diag], [-1, 0, 1], format='csr')
    return D2_1d


class ImplicitSolver:
    # to be added

    def __init__(self):
        self.dt = None
        self.dx = None
        self.indices = None
        self.params = None

        # self.A_u = None
        # self.A_v = None
        # Decomposed matrices
        self.lu_u = None
        self.lu_v = None

    def setup_parameters(self, n, dt, dx, indices, params):
        self.dt = dt
        self.dx = dx
        self.indices = indices
        self.params = params

        A_u = self.generate_evolution_matrix(n, indices, params['d1'])
        A_v = self.generate_evolution_matrix(n, indices, params['d2'])

        # Factorization
        self.lu_u = spla.splu(A_u.tocsc())
        self.lu_v = spla.splu(A_v.tocsc())
        print("Solver parameters set up with LU decomposition.")

    def generate_evolution_matrix(self, n, indices, diff_coef):
        N = n * n

        # --- Identity matrices ---
        I = sp.eye(n)
        I_N_sqr = sp.eye(N)

        # --- 2nd - derivative matrix ---
        # Derv2 = D2(n)
        D2_1d = D2_sparse(n)

        # --- Laplacian ---
        # laplacian = np.kron(I, Derv2) + np.kron(Derv2, I)
        laplacian = sp.kron(I, D2_1d) + sp.kron(D2_1d, I)

        # --- Evolution matrix ---
        factor = (diff_coef * self.dt) / (self.dx**2)
        # A = np.eye(N) - factor * laplacian
        A = (sp.eye(N, format='csr') - factor * laplacian).tolil()

        # --- Replacing the rows of evolution matrix ---
        all_bounds = np.concatenate([indices['l'], indices['r'], indices['t'], indices['b']])
        all_bounds = np.unique(all_bounds)

        for idx in all_bounds:
            A.rows[idx] = [idx]
            A.data[idx] = [1.0]

        return A.tocsr()

    def solve_step(self, u, v, params, dt, dx):
        try:
            u_tmp = u + dt * (params['a'] - u - u * v * v)
            v_tmp = v + dt * (u * v * v - params['m'] * v)
        except:
            raise ValueError("Error in computing the reaction terms during the solver step.")

        # We apply the Dirichlet boundary conditions
        for key in self.indices:
            u_tmp[self.indices[key]] = 0
            v_tmp[self.indices[key]] = 0

        u_next = self.lu_u.solve(u_tmp)
        v_next = self.lu_v.solve(v_tmp)

        return u_next, v_next

if __name__ == "__main__":
    pass