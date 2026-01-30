import numpy as np
import matplotlib.pyplot as plt
from solver import ImplicitSolver
from tqdm import tqdm

class KlausmeierModel:
    def __init__(self, dx, L, a, m, d1=180.0, d2=0.025):
        self.params = {'a': a, 'm': m, 'd1': d1, 'd2': d2}

        self.dx = dx
        self.L = L
        self.n = None

        self.u = None
        self.v = None

        self.bound_indices = None

        self.setup_geometry()

        self.time = 0.0

    def set_a(self, new_a):
        self.params['a'] = new_a

    def setup_geometry(self):
        """
        Preparing the axes, grid and indices for the simulation.
        :return:
        """
        # --- Defining the axes ---
        self.n = int(self.L / self.dx) + 1
        ox = np.linspace(0, self.L, self.n)
        oy = np.linspace(0, self.L, self.n)
        # self.dx = ox[1] - ox[0]

        # --- Defining the grid ---
        X, Y = np.meshgrid(ox, oy)
        X_flat = X.flatten()
        Y_flat = Y.flatten()

        # --- Defining the Dirichlet boundary indices ---
        left_ind = np.where(np.isclose(X_flat, 0, atol=self.dx / 2))[0]
        right_ind = np.where(np.isclose(X_flat, self.L, atol=self.dx / 2))[0]
        top_ind = np.where(np.isclose(Y_flat, self.L, atol=self.dx / 2))[0]
        bot_ind = np.where(np.isclose(Y_flat, 0, atol=self.dx / 2))[0]

        self.bound_indices = {'l': left_ind, 'r': right_ind, 't': top_ind, 'b': bot_ind}

    def set_initial_conditions(self):
        n = self.n
        self.u = (np.full((n, n), 0.70) + np.random.uniform(-0.01, 0.01, (n, n))).flatten()
        self.v = (np.full((n, n), 1.4) + np.random.uniform(-0.01, 0.01, (n, n))).flatten()
        print("Model initial conditions set to: something")

    def step(self, dt, slvr, tolerance):
        self.u, self.v, cont = slvr.solve_step(self.u, self.v, self.params, dt, tolerance)
        self.time += dt
        return cont

    def run_simulation(self, dt, steps, slvr, max_steps = 1000, tolerance = 0):
        if self.time == 0:
            self.set_initial_conditions()
            slvr.setup_parameters(self.n, dt, self.dx, self.bound_indices, self.params)

        n = np.min([steps, max_steps])

        for _ in tqdm(range(n)):
            if not self.step(dt, slvr, tolerance):
                break

        return self.u, self.v

if __name__ == "__main__":

    ht = 0.1
    model = KlausmeierModel(dx=1, L = 250, a=2, m=0.45, d1 = 182.5, d2 = 0.25)
    my_solver = ImplicitSolver()

    """
    model.run_simulation(dt, 0, solver)
    fig, ax = plt.subplots(1, 2)
    im1 = ax[0].imshow(model.u.reshape(model.n, model.n), origin="lower")
    im2 = ax[1].imshow(model.v.reshape(model.n, model.n), origin="lower")
    fig.colorbar(im1, ax=ax[0], fraction=0.046, pad=0.04)
    fig.colorbar(im2, ax=ax[1], fraction=0.046, pad=0.04)
    fig.show()
    """

    model.run_simulation(ht, 100, my_solver, tolerance= 0.001)
    fig, ax = plt.subplots(1, 2)
    im1 = ax[0].imshow(model.u.reshape(model.n, model.n), origin="lower")
    im2 = ax[1].imshow(model.v.reshape(model.n, model.n), origin="lower")
    fig.colorbar(im1, ax=ax[0], fraction=0.046, pad=0.04)
    fig.colorbar(im2, ax=ax[1], fraction=0.046, pad=0.04)
    fig.show()

    u_end, v_end = model.run_simulation(ht, 500, my_solver)
    fig2, ax2 = plt.subplots(1, 2)
    im1 = ax2[0].imshow(model.u.reshape(model.n, model.n), origin="lower")
    im2 = ax2[1].imshow(model.v.reshape(model.n, model.n), origin="lower")
    fig2.colorbar(im1, ax=ax2[0], fraction=0.046, pad=0.04)
    fig2.colorbar(im2, ax=ax2[1], fraction=0.046, pad=0.04)
    fig2.show()

    # print(u_end.reshape(model.n, model.n))