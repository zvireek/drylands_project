import streamlit as st
import sys
import pathlib
import numpy as np
import plotly.express as px

# Ensure project root is available as PROJECT_ROOT (used to find data/)
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

st.title("Klausmeier-Gray-Scott model")

st.markdown("In 1999 Klausmeier published an [article](https://www.science.org/doi/10.1126/science.284.5421.1826) where an example of reaction diffusion models of activator-inhibitor type was formulated. "
         "He was trying to model how plants organize itself in semiarid environment into Turing patters. "
         "\n\n"
         "We know Turing patterns form when a stable system in ODE sense becomes unstable when diffusion term is added. This is widely studied in **Stability analysis** tab. "
         "In this project I tried to analytically examine and simulate which conditions are necessary for Turing patterns to form. For the full instructions on the project go to **Note on the project** tab.")

st.subheader("Turing pattern example")

fish_image = PROJECT_ROOT / "data" / "Giant_Pufferfish.jpg"
if fish_image.exists():
    st.image(str(fish_image), caption=fish_image.name, use_column_width=False)
    st.markdown(r"[By Chiswick Chap - Own work, CC BY-SA 3.0](https://commons.wikimedia.org/w/index.php?curid=19437044)")
else:
    st.info(f"File 'Giant_Pufferfish.jpg' not found in {PROJECT_ROOT / 'data'}")

st.subheader("My simulation result example")

pattern_data = PROJECT_ROOT / "data" / "simulation_a_1.59.csv"
vs = []
try:
    arr = np.loadtxt(pattern_data, delimiter=',')
    if arr.ndim == 1:
        n = int(np.sqrt(arr.size))
        if n * n == arr.size:
            arr = arr.reshape((n, n))
    vs.append(arr)
except Exception as e:
    st.error(f"Error while loading {pattern_data.name}: {e}")
    st.stop()

# display in plotly
try:
    # use the last loaded array (vs[-1]) to build a plotly heatmap
    fig = px.imshow(vs[-1], color_continuous_scale='Viridis', origin='lower')
    fig.update_layout(margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(fig, use_container_width=True)
except Exception as e:
    st.error(f"Error while plotting {pattern_data.name}: {e}")

