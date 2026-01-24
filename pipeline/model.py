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
        ox = np.arange(0, self.L + self.dx, self.dx)
        oy = np.arange(0, self.L + self.dx, self.dx)
        self.dx = ox[1] - ox[0]
        self.n = len(ox)

        # --- Defining the grid ---
        X, Y = np.meshgrid(ox, oy)

        # --- Defining the Dirichlet boundary indices ---
        left_ind = np.isclose(X, 0, atol = self.dx/2).flatten()
        right_ind = np.isclose(X, self.L, atol=self.dx / 2).flatten()
        top_ind = np.isclose(Y, self.L, atol=self.dx / 2).flatten()
        bot_ind = np.isclose(Y, 0, atol=self.dx / 2).flatten()

        sum_indices = left_ind + right_ind + top_ind + bot_ind

        plt.imshow(sum_indices.reshape(self.n, self.n))
        plt.show()

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

    dt = 0.5
    model = KlausmeierModel(dx=0.5, L = 10, a=2.0, m=1, d1 = 1, d2 = 0.01)
    solver = ImplicitSolver()
    model.run_simulation(dt, 2, solver)

    """fig, ax = plt.subplots(1, 2)
    ax[0].imshow(model.u.reshape(model.n, model.n))
    ax[1].imshow(model.v.reshape(model.n, model.n))
    # plt.colorbar()
    fig.show()


    model.run_simulation(dt, 100, solver)

    fig2, ax2 = plt.subplots(1, 2)
    ax2[0].imshow(model.u.reshape(model.n, model.n))
    ax2[1].imshow(model.v.reshape(model.n, model.n))
    # plt.colorbar()
    fig2.show()"""
