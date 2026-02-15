import streamlit as st

st.title("Note on the project")

st.markdown(
    """
    This is my final project for the course "Deterministic modelling".
    
    For the full project description in polish click [here](https://drive.google.com/file/d/1praztb-p7wsZMILljQxAxhEcMCESb9WE/view).
    """)

st.subheader("AI use disclaimer")

st.write("Throughout this project i used AI in debugging the code, making my plots look nicer, "
         "and rewriting my handwritten notes into latex of which results you can see on **1. Theoretical introduction** and **3. Stability analysis.**\n")

st.success("However I would like to stress that I did not use AI to solve any of the problems, write any of the code for simulations which was a purpose of this project, "
         "or make any of the conclusions.")