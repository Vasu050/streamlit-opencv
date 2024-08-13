import streamlit as st
st.markdown("""
    <style>
    /* Apply a red border to the text input box */
    .stTextInput input {
        border: 2px solid red !important;
    }
    /* Ensure the border stays red when the input is focused */
    .stTextInput input:focus {
        border: 2px solid red !important;
        outline: none; /* Remove default focus outline */
    }
    </style>
    """, unsafe_allow_html=True)

st.title('Hello Vasu!')
name = st.text_input('Enter your name')
if name:
   st.write(f'Hello, {name}!')

# Button
if st.button('Say Hello'):
 st.write(f'Hello {name} ')