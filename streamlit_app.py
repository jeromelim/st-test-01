import streamlit as st

st.title("🎈 My First Streamlit App")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}!")

button = st.button("Click me")
if button:
    st.write("I was clicked!")
else:
    st.write("Waiting to be clicked..")

st.checkbox("Check me")