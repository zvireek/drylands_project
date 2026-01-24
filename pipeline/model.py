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

        self.bound_indices = {'l': left_ind, 'r': right_ind, 't': top_ind, 'b': bot_ind}

    def set_initial_conditions(self):
        n = self.n
        self.u = np.ones((n, n)).flatten()
        self.v = np.zeros((n, n)).flatten()
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
    model = KlausmeierModel(dx=0.01, L = 1, a=2.0, m=0.5, d1 = 0.025, d2 = 0.025)
    solver = ImplicitSolver()
    model.run_simulation(0.1, 10, solver)

    plt.imshow(model.u.reshape(model.n, model.n))
    plt.show()

    model.run_simulation(0.1, 10, solver)

    plt.imshow(model.u.reshape(model.n, model.n))
    plt.show()
