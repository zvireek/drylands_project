import streamlit as st

st.write("# 3. Stability analysis")
st.markdown("### When do the patterns form - theoretical analysis.")

st.markdown(r"Turing instability occurs when a stable system in ODE sense turns into unstable one when diffusion term is added. "
            r"A formal analysis of this phenomenon will be conducted in the following way.")

st.markdown("### Steps")
st.markdown("1.  Determining the non-zero, homogeneous equilibrium point $(u^*, v^*) \in \mathbb{R}^2$ of the dimensionless system (4)-(7), such that $v^* > 1$.\n"
            "2.  Linearizing the system around this point and calculating the Jacobian matrix $\mathbf{J}$ for the kinetic (reaction) part.\n"
            "3.  Analyzing stability in the absence of diffusion and showing the conditions that the trace $\\text{tr}(\mathbf{J})$ and determinant $\\text{det}(\mathbf{J})$ must satisfy for the state to be stable.\n"
            "4.  Incorporating diffusion and applying the Fourier method of separation of variables to the linearized system."
            " Considering perturbations in the form of a wave $\mathbf{w}(t, x) \propto e^{\lambda t} e^{ikx}$, substituting them into the linearized equation, and deriving the dispersion relation $\lambda(k)$ as the eigenvalues of the matrix $\mathbf{J} - k^2\mathbf{D}$, where $\mathbf{D}$ is the matrix of diffusion coefficients.\n"
            "5.  Finding analytically and presenting graphically the conditions on parameters for which $\\text{Re}(\lambda(k)) > 0$ for a certain range of wavenumbers $k \\neq 0$ (the condition for pattern formation).")


st.markdown("### Dimensionless form of the model used for analysis")
st.latex(r'''
\begin{cases}
\frac{\partial u}{\partial t} = a - u - uv^2 + d_1 \Delta u & x \in \Omega, \ t > 0 \\
\frac{\partial v}{\partial t} = uv^2 - mv + d_2 \Delta v & x \in \Omega, \ t > 0 \\
u = v = 0 & x \in \partial\Omega, \ t > 0 \\
u(x, 0) = u_0(x), \quad v(x, 0) = v_0(x) & x \in \Omega
\end{cases}
''')

st.divider()

# -----------------------------------------------------------------
st.header("Step 1: Determining the Homogeneous Equilibrium Points")

st.write("""
To find the steady states $(u^*, v^*)$, we set the temporal derivatives and the 
diffusion terms to zero in the dimensionless system:
""")

st.latex(r'''
\begin{cases} 
0 = a - u - uv^2 \\
0 = uv^2 - mv 
\end{cases}
''')

st.write("From the second equation, we have $v(uv - m) = 0$, which leads to two cases:")

st.markdown("#### Case 1: The Desert State")
st.write("""If $v^* = 0$, then $u^* = a$. This corresponds to the **Desert State** $(a, 0)$, which is always stable but does not satisfy the condition $v^* > 1$.""")

st.markdown("#### Case 2: The Vegetated States")
st.write("If $v \\neq 0$, then $u = \\frac{m}{v}$. Substituting this into the first equation:")

st.latex(r'''
a - \frac{m}{v} - \left(\frac{m}{v}\right)v^2 = 0 \implies a - \frac{m}{v} - mv = 0
''')

st.write("Multiplying by $v$ yields the quadratic equation for $v$:")
st.latex(r'''mv^2 - av + m = 0''')

st.write("The discriminant is $\Delta = a^2 - 4m^2$. Real solutions exist only if $a \ge 2m$:")

st.latex(r'''
v^* = \frac{a \pm \sqrt{a^2 - 4m^2}}{2m}
''')

st.write("""
We identify two possible vegetated states. Following the requirement $v^* > 1$, 
we choose the larger root, which corresponds to the **Dense Vegetation** state:
""")

st.latex(r'''
\begin{aligned}
v^* &= \frac{a + \sqrt{a^2 - 4m^2}}{2m} \\[10pt]
u^* &= \frac{m}{v^*} = \frac{2m^2}{a + \sqrt{a^2 - 4m^2}}
\end{aligned}
''')

st.success(f"This equilibrium point $(u^*, v^*)$ exists and satisfies $v^* > 1$ provided that $a > 2m$.")

# ---------------------------------------------------------
st.header("Step 2: Linearization and the Jacobian Matrix")

st.write(r"""
To analyze the stability of the system, we linearize the kinetic equations 
$f(u, v)$ and $g(u, v)$ around the equilibrium point $(u^*, v^*)$:
""")

st.latex(r'''
\begin{aligned}
f(u, v) &= a - u - uv^2 \\
g(u, v) &= uv^2 - mv
\end{aligned}
''')

st.write("We calculate the partial derivatives to form the Jacobian matrix:")

col1, col2 = st.columns(2)
with col1:
    st.latex(r'''
    \begin{aligned}
    f_u &= -1 - v^2 \\
    f_v &= -2uv
    \end{aligned}
    ''')
with col2:
    st.latex(r'''
    \begin{aligned}
    g_u &= v^2 \\
    g_v &= 2uv - m
    \end{aligned}
    ''')

st.write(r"At the equilibrium point, we know that $u^*v^* = m$. Therefore, $2u^*v^* = 2m$. Substituting these into the Jacobian matrix $\mathbf{J}$:")

st.latex(r'''
J(u^*, v^*) = \begin{pmatrix} 
f_u & f_v \\ 
g_u & g_v 
\end{pmatrix} = 
\begin{pmatrix} 
-1 - (v^*)^2 & -2m \\ 
(v^*)^2 & m 
\end{pmatrix}
''')

st.write("Substituting the explicit value of $v^* = \\frac{a + \sqrt{a^2 - 4m^2}}{2m}$, we get:")

st.latex(r'''
J = \begin{pmatrix} 
-1 - \frac{(a + \sqrt{a^2 - 4m^2})^2}{4m^2} & -2m \\ 
\frac{(a + \sqrt{a^2 - 4m^2})^2}{4m^2} & m 
\end{pmatrix}
''')

st.markdown("#### The Characteristic Equation")
st.write(r"The stability is determined by the eigenvalues $\lambda$, found by solving $\det(J - \lambda I) = 0$:")

st.latex(r'''
\lambda^2 - (f_u + g_v)\lambda + (f_u g_v - f_v g_u) = 0
''')

st.info(r"""
**Note:** In the context of stability:
- The Trace is $\text{tr}(J) = f_u + g_v$
- The Determinant is $\det(J) = f_u g_v - f_v g_u$
""")

# ------------------------------------------------------------
st.header("Step 3: Stability Analysis (Without Diffusion)")

st.write(r"""
Following the reasoning presented by Kanako Suzuki, the characteristic equation 
will have two roots with negative real parts, $\text{Re}(\lambda) < 0$, 
if and only if the following conditions are met:
""")

st.latex(r'''
\underbrace{f_u + g_v < 0}_{\text{tr}(J)} \quad \text{and} \quad \underbrace{f_u g_v - f_v g_u > 0}_{\det(J)}
''')

st.markdown("#### 1. Analyzing the Trace Condition ($\\text{tr}(J) < 0$)")
st.write("Substituting the values at the equilibrium point:")
st.latex(r'''
\text{tr}(J) = -1 - (v^*)^2 + m < 0 \implies (v^*)^2 > m - 1
''')

st.write("Expanding $(v^*)^2$ using the value found in Step 1:")
st.latex(r'''
\begin{aligned}
\frac{(a + \sqrt{a^2 - 4m^2})^2}{4m^2} &> m - 1 \\[10pt]
\frac{a^2 + 2a\sqrt{a^2 - 4m^2} + a^2 - 4m^2}{4m^2} &> m - 1 \\[10pt]
2a^2 + 2a\sqrt{a^2 - 4m^2} - 4m^2 &> 4m^3 - 4m^2 \\[10pt]
2a^2 + 2a\sqrt{a^2 - 4m^2} &> 4m^3
\end{aligned}
''')

st.markdown("#### 2. Analyzing the Determinant Condition ($\det(J) > 0$)")
st.write(r"Using the relationship $u^*v^* = m$ at equilibrium, the determinant simplifies:")
st.latex(r'''
\begin{aligned}
\det(J) &= (-1 - (v^*)^2)m + 2m(v^*)^2 > 0 \\
&= -m - m(v^*)^2 + 2m(v^*)^2 > 0 \\
&= m(v^*)^2 - m > 0 \\
&\implies (v^*)^2 > 1
\end{aligned}
''')
st.write("Since we previously established that $v^* > 1$ for the dense vegetation state, this condition is **always satisfied**.")

st.markdown("#### Summary of Kinetic Stability")
st.success(r"""
The homogeneous equilibrium point $(u^*, v^*)$ is stable in the absence of diffusion if:
1. $a > 2m$ (Existence condition)
2. $(v^*)^2 > m - 1$ (Trace condition)
""")

# ---------------------------------------------------------
st.header("Step 4: Incorporating diffusion")

st.write(r"""
To analyze the effect of spatial dynamics, we introduce small perturbations $(z, w)$ 
around the homogeneous equilibrium point $(u^*, v^*)$:
""")

st.latex(r'''
u(x, t) = u^* + \epsilon z(x, t), \quad v(x, t) = v^* + \epsilon w(x, t)
''')

st.write("Substituting these into the model and linearizing, we obtain the system of PDEs:")

st.latex(r'''
\begin{cases}
\frac{\partial z}{\partial t} = d_1 \frac{\partial^2 z}{\partial x^2} + f_u(u^*, v^*)z + f_v(u^*, v^*)w \\[8pt]
\frac{\partial w}{\partial t} = d_2 \frac{\partial^2 w}{\partial x^2} + g_u(u^*, v^*)z + g_v(u^*, v^*)w
\end{cases}
''')

st.write("With Neumann boundary conditions: $\\frac{\partial z}{\partial x} = \\frac{\partial w}{\partial x} = 0$ at the boundaries.")

st.markdown("#### Fourier Separation of Variables")
st.write(r"""
Applying the method of separation of variables, we expand the perturbations 
into a Fourier cosine series to satisfy the boundary conditions:
""")

st.latex(r'''
z(x, t) = \sum_{n=0}^{\infty} z_n(t) \cos\left(\frac{\pi n}{L}x\right), \quad 
w(x, t) = \sum_{n=0}^{\infty} w_n(t) \cos\left(\frac{\pi n}{L}x\right)
''')

st.write(r"After transformation, the dynamics for each mode $n$ are governed by the following system of ODEs:")

st.latex(r'''
\frac{d}{dt} \begin{pmatrix} z_n \\ w_n \end{pmatrix} = 
\begin{pmatrix} 
-d_1 \left(\frac{\pi n}{L}\right)^2 + f_u & f_v \\ 
g_u & -d_2 \left(\frac{\pi n}{L}\right)^2 + g_v 
\end{pmatrix} 
\begin{pmatrix} z_n \\ w_n \end{pmatrix}
''')

st.info(r"""
**Note:** The matrix above is often denoted as $J_k$, where $k = \frac{\pi n}{L}$ 
is the wavenumber. Turing instability occurs if this matrix has at least 
one eigenvalue with $\text{Re}(\lambda) > 0$ for $k > 0$, while being stable for $k=0$.
""")

st.write("One can notice that we can already write this matrix in the following form, which will be useful in the next step:")

st.latex(r'''
\frac{d}{dt} \begin{pmatrix} z_n \\ w_n \end{pmatrix} = (J - k^2 D) \begin{pmatrix} z_n \\ w_n \end{pmatrix}
''')

st.write(r"where $k = \frac{\pi n}{L}$ is the wavenumber and $D = \text{diag}(d_1, d_2)$ is the diffusion matrix.")
