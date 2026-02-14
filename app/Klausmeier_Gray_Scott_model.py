import streamlit as st
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pipeline.model import KlausmeierModel
from pipeline.solver import ImplicitSolver

st.title("Klausmeier-Gray-Scott model")

st.write("I'll finish tomorrow. :D")