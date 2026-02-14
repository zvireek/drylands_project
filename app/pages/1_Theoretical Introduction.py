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

st.markdown(r"In order to efficiently run the simulations the number of parameters must be reduced through dimensionless analysis which will lead to this form with only 2 parameters - $a, m$.")

st.latex(r'''
\begin{cases}
\frac{\partial u}{\partial t} = a - u - uv^2 + d_1 \Delta u & x \in \Omega, \ t > 0 \\
\frac{\partial v}{\partial t} = uv^2 - mv + d_2 \Delta v & x \in \Omega, \ t > 0 \\
u = v = 0 & x \in \partial\Omega, \ t > 0 \\
u(x, 0) = u_0(x), \quad v(x, 0) = v_0(x) & x \in \Omega
\end{cases}
''')


st.markdown("### Substitution")
st.markdown(
    r"""    
    The following substitution is proposed:
    $$
    W = W_0u, \quad N = N_0v, \quad T = T_0t, \quad X = X_0x,
    $$
    where $W_0, N_0, T_0, X_0$ are scaling constants.
    """
)

st.markdown("One can write it in a different form so that it is easier to differentiate by the chain rule.")

st.latex(r'''
u(t) = \frac{W(T(t))}{W_0}, \quad 
v(t) = \frac{N(T(t))}{N_0}, \quad 
t = \frac{T}{T_0}, \quad 
x = \frac{X}{X_0}
''')

st.divider()

st.markdown("### 1.1. Calculating derivatives")

st.markdown("##### Time derivatives")
# st.markdown("""Using this proposition we calculate time derivatives:""")

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

st.markdown("That leads to:")

st.latex(r'''
\begin{cases} 
\frac{\partial u}{\partial t} = \frac{T_0}{W_0} \cdot \frac{\partial W}{\partial T} \\[8pt]
\frac{\partial v}{\partial t} = \frac{T_0}{N_0} \cdot \frac{\partial N}{\partial T}
\end{cases}
''')

st.markdown("##### Space derivatives")
st.markdown("For W:")

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

st.latex(r"\Delta N = \frac{N_0}{X_0^2} \Delta v.")

st.divider()

st.markdown("### 1.2. Substituting into original model")

# Step 2: Full substitution
# st.write("Substituting the original model equations:")
st.latex(r'''
\begin{cases} 
\frac{\partial u}{\partial t} = \frac{T_0}{W_0} \left( A - L \cdot W_0 u - R W_0 u (N_0 v)^2 + D_W \cdot \frac{W_0}{X_0^2} \Delta u \right) \\[10pt]
\frac{\partial v}{\partial t} = \frac{T_0}{N_0} \left( J R W_0 u (N_0 v)^2 - M N_0 v + D_N \cdot \frac{N_0}{X_0^2} \Delta v \right) 
\end{cases}
''')

# Step 3: Simplified version
st.write("Simplifying by distributing the constants:")
st.latex(r'''
\begin{cases} 
\frac{\partial u}{\partial t} = T_0 \left( \frac{A}{W_0} - L u - R u N_0^2 v^2 + D_W \cdot \frac{1}{X_0^2} \Delta u \right) \\[10pt]
\frac{\partial v}{\partial t} = T_0 \left( J R W_0 N_0 u v^2 - M v + D_N \frac{1}{X_0^2} \Delta v \right) 
\end{cases}
''')


# Step 4: Choosing constants
st.markdown("##### Defining Parameter Constraints")
st.write("To achieve a dimensionless form of the system we choose the scaling constants such that the following relations hold:")

col1, col2 = st.columns(2)

with col1:
    st.latex(r'''
    \begin{aligned}
    a &= \frac{T_0}{W_0} A \\
    1 &= T_0 L \\
    1 &= T_0 R N_0^2 \\
    d_1 &= D_W \cdot \frac{T_0}{X_0^2}
    \end{aligned}
    ''')

with col2:
    st.latex(r'''
    \begin{aligned}
    1 &= T_0 J R W_0 N_0 \\
    m &= T_0 M \\
    d_2 &= \frac{T_0}{X_0^2} D_N
    \end{aligned}
    ''')

st.markdown("##### Solving for Constants")
st.write("From the constraints above, we derive the following values for our scaling factors:")

col3, col4 = st.columns(2)

with col3:
    st.latex(r'''
    \begin{aligned}
    T_0 &= \frac{1}{L} \\[5pt]
    N_0 &= \sqrt{\frac{L}{R}} \\[5pt]
    d_1 &= \frac{D_W}{L X_0^2}
    \end{aligned}
    ''')

with col4:
    st.latex(r'''
    \begin{aligned}
    m &= \frac{M}{L} \\[5pt]
    d_2 &= \frac{D_N}{L X_0^2}
    \end{aligned}
    ''')

st.markdown("##### Calculating $W_0$ and $a$")
st.write("Substituting $T_0$ and $N_0$ into the equation for $W_0$:")

st.latex(r'''
1 = \frac{1}{L} J R W_0 \sqrt{\frac{L}{R}} \implies W_0 = \frac{L \sqrt{R}}{J R \sqrt{L}} = \frac{1}{J} \sqrt{\frac{L}{R}}
''')

# Final version
st.write("Finally, the dimensionless precipitation $a$ is given by:")
st.latex(r'''
a = \frac{T_0}{W_0} A = \frac{J A}{L} \sqrt{\frac{R}{L}}
''')

st.markdown("### 1.3. Final Summary of Scaling and Parameters")
st.write("Therefore, the complete set of substitutions and parameters is:")

# Create two columns to mimic the boxes in your notes
col1, col2 = st.columns(2)

with col1:
    st.info("**Dimensionless Parameters**")
    st.latex(r'''
    \begin{aligned}
    a &= \frac{J \cdot A}{L} \sqrt{\frac{R}{L}} \\[10pt]
    m &= \frac{M}{L} \\[10pt]
    d_1 &= \frac{D_W}{L X_0^2} \\[10pt]
    d_2 &= \frac{D_N}{L X_0^2}
    \end{aligned}
    ''')

with col2:
    st.info("**Scaling Constants**")
    st.latex(r'''
    \begin{aligned}
    T_0 &= \frac{1}{L} \\[10pt]
    N_0 &= \sqrt{\frac{L}{R}} \\[10pt]
    W_0 &= \frac{1}{J} \sqrt{\frac{L}{R}}
    \end{aligned}
    ''')