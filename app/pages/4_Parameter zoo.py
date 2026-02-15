import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import pathlib
import sys
import re

# st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
        .main .block-container {
            max-width: 95rem;
            padding-top: 5rem;
            padding-right: 1rem;
            padding-left: 1rem;
            padding-bottom: 5rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("# 4. Parameter zoo")

st.info("This page may take a second to load.")

params = {
    "Parameter": ["dx", "L", "a_start", "a_end", "m", "d1", "d2"],
    "Value": [0.25, 100, 0, 1.7, 0.45, 2, 0.01],
    "Description": [
        "Space step size",
        "Domain length",
        "Precipitation (start value)",
        "Precipitation (end value)",
        "Plant mortality",
        "Water diffusion coefficient",
        "Plant diffusion coefficient"
    ]
}

df = pd.DataFrame(params)

st.dataframe(
    df,
    column_config={
        "Value": st.column_config.NumberColumn(
            format="%.2f",
        )
    },
    hide_index=True,
    use_container_width=True
)

st.success("**TIP**: Use zoom option (second from left on the toolbar in the top right) to see a pattern clearly!")

# Ensure project root is available
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Find and load simulation CSV files
DATA_DIR = PROJECT_ROOT / "data"
pattern = re.compile(r"simulation_a_([-+]?[0-9]*\.?[0-9]+)\.csv")
files = []
if DATA_DIR.exists():
    for p in sorted(DATA_DIR.iterdir()):
        m = pattern.match(p.name)
        if m and p.is_file():
            try:
                a_val = float(m.group(1))
                files.append((a_val, p))
            except Exception:
                continue

if not files:
    st.error(f"Nie znaleziono plików CSV w {DATA_DIR} pasujących do 'simulation_a_*.csv'.")
    st.stop()

# Sort and Load Data
files.sort(key=lambda x: x[0])
a_values = [a for a, p in files]

vs = []
for a, p in files:
    try:
        arr = np.loadtxt(p, delimiter=',')
        if arr.ndim == 1:
            n = int(np.sqrt(arr.size))
            if n * n == arr.size:
                arr = arr.reshape((n, n))
        vs.append(arr)
    except Exception as e:
        st.error(f"Błąd podczas wczytywania {p.name}: {e}")
        st.stop()

# Grid Calculation
num_plots = len(vs)
num_cols = 4
num_rows = (num_plots + num_cols - 1) // num_cols

# Create subplots
fig = make_subplots(
    rows=num_rows, cols=num_cols,
    subplot_titles=[f'a = {a:.2f}' for a in a_values],
    horizontal_spacing=0.05,
    vertical_spacing=0.1
)

# Shared Color limits
vmin = 0
try:
    vmax = max(np.nanmax(arr) for arr in vs)
except Exception:
    vmax = 1.0

for i in range(num_plots):
    row = (i // num_cols) + 1
    col = (i % num_cols) + 1

    # Add heatmap trace
    fig.add_trace(
        go.Heatmap(
            z=vs[i],
            colorscale='Viridis',
            coloraxis="coloraxis", # Link all heatmaps to one shared coloraxis
        ),
        row=row, col=col
    )

    # Apply the anchor to EVERY subplot axis individually
    fig.update_xaxes(
        showticklabels=False, showgrid=False, zeroline=False,
        row=row, col=col
    )
    fig.update_yaxes(
        showticklabels=False, showgrid=False, zeroline=False,
        scaleanchor=f"x{i+1 if i>0 else ''}", # Anchors this y-axis to the corresponding x-axis
        scaleratio=1,
        row=row, col=col
    )

# Use coloraxis for a single shared colorbar
fig.update_layout(
    coloraxis=dict(
        colorscale='Viridis',
        cmin=vmin,
        cmax=vmax,
        colorbar=dict(
            title='Vegetation Density (v)',
            thickness=20,
            len=0.8,
            y=0.5
        )
    ),
    title_text='Simulation Results for Different a Values',
    height=700 * num_rows, # Dynamically adjust height based on rows to keep them square
    showlegend=False,
    margin=dict(l=50, r=50, t=100, b=50)
)

st.plotly_chart(fig, use_container_width=True)