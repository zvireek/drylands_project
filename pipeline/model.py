import numpy as np
import matplotlib.pyplot as plt
from solver import ImplicitSolver

class KlausmeierModel:
    def __init__(self, dx, L, a, m, d1=0.025, d2=0.025):
        self.params = {'a': a, 'm': m, 'd1': d1, 'd2': d2}

        self.dx = dx
        self.L = L
        self.n = None

        self.u = None
        self.v = None

        self.bound_indices = None

        self.setup_geometry()

        self.time = 0.0

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

        # --- Defining the Dirichlet boundary indices ---
        left_ind = np.isclose(X, 0, atol = self.dx/2).flatten()
        right_ind = np.isclose(X, self.L, atol=self.dx / 2).flatten()
        top_ind = np.isclose(Y, self.L, atol=self.dx / 2).flatten()
        bot_ind = np.isclose(Y, 0, atol=self.dx / 2).flatten()

        self.bound_indices = {'l': left_ind, 'r': right_ind, 't': top_ind, 'b': bot_ind}

    def set_initial_conditions(self):
        n = self.n
        self.u = (np.full((n, n), 0.70) + np.random.uniform(-0.01, 0.01, (n, n))).flatten()
        self.v = (np.full((n, n), 1.4) + np.random.uniform(-0.01, 0.01, (n, n))).flatten()
        print("Model initial conditions set to: something")

    def step(self, dt, solver):
        self.u, self.v = solver.solve_step(self.u, self.v, self.params, dt, self.dx)
        self.time += dt

    def run_simulation(self, dt, steps, solver):
        if self.time == 0:
            self.set_initial_conditions()
            solver.setup_parameters(self.n, dt, self.dx, self.bound_indices, self.params)

        for _ in range(steps):
            self.step(dt, solver)

if __name__ == "__main__":

    dt = 0.1
    model = KlausmeierModel(dx=0.1, L = 2, a=2.0, m=1, d1 = 100, d2 = 1)
    solver = ImplicitSolver()

    model.run_simulation(dt, 0, solver)
    fig, ax = plt.subplots(1, 2)
    im1 = ax[0].imshow(model.u.reshape(model.n, model.n))
    im2 = ax[1].imshow(model.v.reshape(model.n, model.n))
    fig.colorbar(im1, ax=ax[0], fraction=0.046, pad=0.04)
    fig.colorbar(im2, ax=ax[1], fraction=0.046, pad=0.04)
    fig.show()

    model.run_simulation(dt, 1, solver)
    fig, ax = plt.subplots(1, 2)
    im1 = ax[0].imshow(model.u.reshape(model.n, model.n))
    im2 = ax[1].imshow(model.v.reshape(model.n, model.n))
    fig.colorbar(im1, ax=ax[0], fraction=0.046, pad=0.04)
    fig.colorbar(im2, ax=ax[1], fraction=0.046, pad=0.04)
    fig.show()


    model.run_simulation(dt, 100, solver)
    fig2, ax2 = plt.subplots(1, 2)
    im1 = ax2[0].imshow(model.u.reshape(model.n, model.n))
    im2 = ax2[1].imshow(model.v.reshape(model.n, model.n))
    fig2.colorbar(im1, ax=ax2[0], fraction=0.046, pad=0.04)
    fig2.colorbar(im2, ax=ax2[1], fraction=0.046, pad=0.04)
    fig2.show()
