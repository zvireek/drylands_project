import streamlit as st


st.write("# 1. Dimensionless form of the model")

st.markdown(
    """
    The original Klausmeier model is given by the following system of differential equations:
    """
)

st.latex(r'''
\begin{cases} 
    \frac{\partial W}{\partial T} = A - LW - RWN^2 + D_W \Delta W \\ 
    \frac{\partial N}{\partial T} = JRWN^2 - MN + D_N \Delta N 
\end{cases}
''')

st.markdown(
    r"""
    In order to efficiently run the simulations the number of parameters must be reduced through dimensionless analysis.
    
    The following substitution is proposed:
    $$
    W = W_0u, \quad N = N_0v, \quad T = T_0t, \quad X = X_0x,
    $$
    where $W_0, N_0, T_0, X_0$ are scaling constants.
    """
)

st.divider()

st.markdown("""Using this proposition we calculate time derivatives:""")

st.latex(r'''
\begin{aligned}
    \frac{\partial u}{\partial t} = \frac{\partial}{\partial t} \frac{W(T)}{W_0} =
    \frac{1}{W_0} \frac{\partial}{\partial t} W(T(t)) = \frac{1}{W_0} \frac{\partial W}{\partial T} \frac{\partial T}{\partial t} =
    \frac{T_0}{W_0} \frac{\partial W}{\partial T}
\end{aligned}
''')

st.latex(r'''
\begin{aligned}
    \frac{\partial v}{\partial t} = \frac{\partial}{\partial t} \frac{N(T)}{N_0} =
    \frac{1}{N_0} \frac{\partial}{\partial t} N(T(t)) = \frac{1}{N_0} \frac{\partial N}{\partial T} \frac{\partial T}{\partial t} =
    \frac{T_0}{N_0} \frac{\partial N}{\partial T}
\end{aligned}
''')

st.markdown("and space derivatives for W:")

# Derivation for W
st.latex(r'''
\begin{aligned}
\frac{\partial W}{\partial X} &= \frac{\partial}{\partial X} \cdot W_0 u(x) = W_0 \cdot \frac{\partial u}{\partial x} \cdot \frac{\partial x}{\partial X} = \frac{W_0}{X_0} \cdot \frac{\partial u}{\partial x} \\[15pt]
\frac{\partial^2 W}{\partial X^2} &= \frac{\partial}{\partial X} \cdot \left( \frac{W_0}{X_0} \cdot \frac{\partial u}{\partial x} \right) = \frac{W_0}{X_0} \cdot \frac{\partial}{\partial X} \cdot \left( \frac{\partial u}{\partial x} \right) = \frac{W_0}{X_0} \cdot \left( \frac{\partial x}{\partial X} \cdot \frac{\partial}{\partial x} \right) \cdot \frac{\partial u}{\partial x} = \frac{W_0}{X_0^2} \cdot \frac{\partial^2 u}{\partial x^2}
\end{aligned}
''')

st.latex(r"\Delta W = \frac{W_0}{X_0^2} \Delta u")

st.markdown("and for N:")

st.latex(r'''
\begin{aligned}
\frac{\partial N}{\partial X} &= \frac{\partial}{\partial X} N_0 v(x) = N_0 \frac{\partial v}{\partial x} \cdot \frac{\partial x}{\partial X} = \frac{N_0}{X_0} \cdot \frac{\partial v}{\partial x} \\[15pt]
\frac{\partial^2 N}{\partial X^2} &= \frac{\partial}{\partial X} \left( \frac{N_0}{X_0} \cdot \frac{\partial v}{\partial x} \right) = \frac{N_0}{X_0} \left( \frac{\partial}{\partial X} \cdot \frac{\partial v}{\partial x} \right) = \frac{N_0}{X_0} \cdot \left( \frac{\partial x}{\partial X} \cdot \frac{\partial}{\partial x} \right) \cdot \frac{\partial v}{\partial x} = \frac{N_0}{X_0^2} \cdot \frac{\partial^2 v}{\partial x^2}
\end{aligned}
''')

st.latex(r"\Delta N = \frac{N_0}{X_0^2} \Delta v")