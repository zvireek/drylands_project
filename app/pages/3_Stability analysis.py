import streamlit as st

st.write("# 3. Stability analysis")
st.subheader("When do the patterns form - theoretical analysis.")

st.markdown(r"Turing instability occurs when a stable system in ODE sense turns into unstable one when diffusion term is added. "
            r"A formal analysis of this phenomenon will be conducted in the following way.")

st.subheader("Steps")
st.markdown("1.  Determining the non-zero, homogeneous equilibrium point $(u^*, v^*) \in \mathbb{R}^2$ of the dimensionless system (4)-(7), such that $v^* > 1$.\n"
            "2.  Linearizing the system around this point and calculating the Jacobian matrix $\mathbf{J}$ for the kinetic (reaction) part.\n"
            "3.  Analyzing stability in the absence of diffusion and showing the conditions that the trace $\\text{tr}(\mathbf{J})$ and determinant $\\text{det}(\mathbf{J})$ must satisfy for the state to be stable.\n"
            "4.  Incorporating diffusion and applying the Fourier method of separation of variables to the linearized system."
            " Considering perturbations in the form of a wave $\mathbf{w}(t, x) \propto e^{\lambda t} e^{ikx}$, substituting them into the linearized equation, and deriving the dispersion relation $\lambda(k)$ as the eigenvalues of the matrix $\mathbf{J} - k^2\mathbf{D}$, where $\mathbf{D}$ is the matrix of diffusion coefficients.\n"
            "5.  Finding analytically and presenting graphically the conditions on parameters for which $\\text{Re}(\lambda(k)) > 0$ for a certain range of wavenumbers $k \\neq 0$ (the condition for pattern formation).")