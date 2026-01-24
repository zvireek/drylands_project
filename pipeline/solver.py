import numpy as np
import scipy.sparse as sp

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


class ImplicitSolver:
    # to be added

    def __init__(self):
        self.dt = None
        self.dx = None
        self.indices = None
        self.params = None
        self.ev_mtr1 = None
        self.ev_mtr2 = None

    def setup_parameters(self, n, dt, dx, indices, params):
        self.dt = dt
        self.dx = dx
        self.indices = indices
        self.params = params
        self.ev_mtr1 = self.generate_evolution_matrix(n, indices, params['d1'])
        self.ev_mtr2 = self.generate_evolution_matrix(n, indices, params['d2'])
        print("Solver parameters set up.")

    def generate_evolution_matrix(self, n, indices, diff_coef):
        N = n * n

        # --- Identity matrices ---
        I = np.eye(n)
        I_N_sqr = np.eye(N)

        # --- 2nd - derivative matrix ---
        Derv2 = D2(n)

        # --- Laplacian ---
        laplacian = np.kron(I, Derv2) + np.kron(Derv2, I)

        # --- Evolution matrix ---
        factor = (diff_coef * self.dt) / (self.dx**2)
        A = np.eye(N) - factor * laplacian

        # --- Replacing the rows of evolution matrix ---
        A[indices['l'], :] = I_N_sqr[indices['l'],]
        A[indices['r'], :] = I_N_sqr[indices['r'],]
        A[indices['t'], :] = I_N_sqr[indices['t'],]
        A[indices['b'], :] = I_N_sqr[indices['b'],]

        return sp.csr_matrix(A)

    def solve_step(self, u, v, params, dt, dx):
        u_tmp = u.copy()
        v_tmp = v.copy()

        # We apply the Dirichlet boundary conditions
        for key in self.indices:
            u_tmp[self.indices[key]] = 0
            v_tmp[self.indices[key]] = 0

        u = sp.linalg.spsolve(self.ev_mtr1, u_tmp)
        v = sp.linalg.spsolve(self.ev_mtr2, v_tmp)

        return u, v

if __name__ == "__main__":
    pass