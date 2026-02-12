import streamlit as st
import sys
import pathlib

# Ensure project root is on sys.path so `from pipeline...` works even when
# Streamlit is launched from a subdirectory.
ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pipeline.model import KlausmeierModel
from pipeline.solver import ImplicitSolver

st.title("Klausmeier-Gray-Scott model")
st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun.

    **There's :rainbow[so much] you can build!**

    We prepared a few examples for you to get started. Just 
    click on the buttons above and discover what you can do 
    with Streamlit. 
    """
)

st.markdown(
    r"""
    Metoda niejawna polega na przybliżaniu funkcji za pomocą wzoru
    $$
    u(X, t + h_t) = u(X, t) + h_t \Delta u(X, t + h_t)
    $$
    W przestrzenii dyskretnej nasze równanie ciepła przyjmuje postać:
    $$
    u(X, t+h_t) = u(X, t) + \alpha \frac{h_t}{h_x^2} \overset{\sim}{\Delta} u(X, t+h_t)
    $$
    gdzie
    $$
    \overset{\sim}{\Delta} = I_{N}\otimes D_2(N_x) + D_2(N_y) \otimes I_{N}.
    $$
    co po przekształceniu daje nam:
    $$
    u(X, t+h_t) (Id - \alpha \frac{h_t}{h_x^2} \overset{\sim}{\Delta}) = u(X, t)
    $$
    """
)


if st.button("Send balloons!"):
    st.balloons()

# Przykladowe użycie KlausmeierModel i ImplicitSolver w Streamlit
if st.button("Uruchom krótką symulację"):
    # Parametry (dostosuj do potrzeb)
    dx = 1.0
    L = 20.0
    a = 1.0
    m = 0.45
    d1 = 80.0
    d2 = 1.0
    dt = 0.1
    steps = 50

    try:
        model = KlausmeierModel(dx=dx, L=L, a=a, m=m, d1=d1, d2=d2)
        solver = ImplicitSolver()
        # solver musi zostać przygotowany przy pierwszym kroku: setup_parameters wywoływane jest w model.run_simulation
        u_end, v_end = model.run_simulation(dt, steps, solver, tolerance=0.0, verbose=False)
        # Wyświetlamy końcowy stan (przekształcamy do macierzy n x n)
        n = model.n
        st.write("Średnia v:", float(v_end.mean()))
        st.image((v_end.reshape(n, n)), caption="v (end)", clamp=True)
    except Exception as e:
        st.error(f"Wystąpił błąd podczas symulacji: {e}")
