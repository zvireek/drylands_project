import streamlit as st
import pandas as pd
import sys
import pathlib

# Ensure project root is available as PROJECT_ROOT (used to find data/)
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

st.write("# 2. Bifurcation diagram")

st.markdown("We want to create a bifurcation diagram in order to see how the $a$ - rain parameter "
            "influences the biomass level (measured by mean of a domain and maximum value).")

st.markdown("It is done in the following way:\n"
            "1. Choose high $a$ (humid conditions).\n"
            "2. Solve the system until it reaches a stable point and measure necessary values (mean, max).\n"
            "3. Reduce slightly value of $a$.\n"
            "4. Run the simulation taking final state from the previous step as initial condition.\n"
            "5. Repeat the procedure until it reaches $a = 0$."
            )

st.subheader("Simulation Parameters")

# Create a dictionary of your parameters
params = {
    "Parameter": ["dx", "L", "a_start", "a_end", "m", "d1", "d2"],
    "Value": [0.5, 50, 1.5, 0, 0.45, 1, 0.05],
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


# Display the bifurcation diagram image from project data/
bif_image = PROJECT_ROOT / "data" / "bif_diag.png"
if bif_image.exists():
    st.subheader("Bifurcation diagram")
    st.image(str(bif_image), caption=bif_image.name, use_column_width=True)
else:
    st.info(f"Plik 'bif_diag.png' nie został znaleziony w {PROJECT_ROOT / 'data'}")

# Display the pre-computed video (search in project data/ first, then app/)
app_dir = pathlib.Path(__file__).resolve().parent
data_video_path = PROJECT_ROOT / "data" / "klausmeier_animation.mp4"
app_video_path = app_dir / "klausmeier_animation.mp4"

video_path = None
if data_video_path.exists():
    video_path = data_video_path
elif app_video_path.exists():
    video_path = app_video_path

if video_path is not None:
    try:
        st.video(str(video_path))
    except Exception:
        try:
            with open(video_path, 'rb') as f:
                video_bytes = f.read()
            st.video(video_bytes)
        except Exception as e:
            st.error(f"Nie udało się odtworzyć wideo ({video_path}): {e}")
else:
    st.warning(f"Plik wideo nie został znaleziony w 'data/' ani w 'app/'. Szukane ścieżki:\n  {data_video_path}\n  {app_video_path}")