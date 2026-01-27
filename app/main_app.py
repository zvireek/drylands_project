import streamlit as st

st.title("Hello Streamlit-er 👋")
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
