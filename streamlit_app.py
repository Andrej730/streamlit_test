import streamlit as st

def process_text(text: str) -> str:
    return text.upper()

st.title("Text Processor App")

user_input = st.text_input("Enter some text:")
if st.button("Process"):
    result = process_text(user_input)
    st.write("Processed text:", result)
