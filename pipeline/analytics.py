import numpy as np
import matplotlib.pyplot as plt
from solver import ImplicitSolver
from model import KlausmeierModel


def bifurcation_diagram(a_start = 0, a_end = 1.2):
    a_vals = np.linspace(a_end, a_start, 30, endpoint=False)
    dt = 0.05
    imp_solver = ImplicitSolver()
    klaus_model = KlausmeierModel(dx=0.25, L=10, a=a_end, m=0.45, d1=1, d2 = 0.05)
    maxes = []
    avs = []
    vs = []

    for aa in a_vals:
        u_end, v_end = klaus_model.run_simulation(dt, 1000, imp_solver, tolerance = 0)
        maxes.append(np.max(v_end))
        avs.append(np.average(v_end))
        vs.append(v_end)
        klaus_model.set_a(aa)

    return a_vals, maxes, avs, vs


x_vals, m, a, vs = bifurcation_diagram()
plt.scatter(x_vals, m, label='Maxes')
plt.scatter(x_vals, a, label='Averages')
plt.xlabel('Parameter a')
plt.ylabel('Value')
plt.legend()
plt.show()