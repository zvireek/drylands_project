from model import KlausmeierModel
from solver import ImplicitSolver
import numpy as np
import matplotlib.pyplot as plt
from tqdm.auto import tqdm

# Defining parameters
dt, steps = 0.1, 1000
dx, L = 0.5, 20
N = int(L/dx) + 1
m = 0.45
d1, d2 = 2, 0.01

a_values = np.linspace(1, 2, num=16)

imp_solver = ImplicitSolver()
vs = []

for a in tqdm(a_values):
  klaus_model = KlausmeierModel(dx, L, a, m, d1, d2)
  u_end, v_end = klaus_model.run_simulation(dt, steps, imp_solver, tolerance = 0, verbose=False)
  vs.append(v_end.reshape(N, N))

fig, axes = plt.subplots(4, 4, figsize=(12, 10))
axes = axes.flatten()

vmin = 0
vmax = np.max(vs)

for i in range(len(vs)):
    im = axes[i].imshow(vs[i], vmin=vmin, vmax=vmax, cmap='viridis')
    axes[i].set_title(f'a = {a_values[i]:.2f}')
    axes[i].axis('off')
    axes[i].set_aspect('equal')

fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.88, 0.15, 0.03, 0.7])
fig.colorbar(im, cax=cbar_ax)

plt.show()