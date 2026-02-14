import streamlit as st
import pandas as pd


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
    "Parameter": ["dx", "L", "a", "m", "d1", "d2"],
    "Value": [0.5, 100, 1.0, 0.45, 4, 0.02],
    "Description": [
        "Space step size",
        "Domain length",
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
            format="%.2f",  # This sets 2 decimal places. Use %.3f for three.
        )
    },
    hide_index=True,
    use_container_width=True
)