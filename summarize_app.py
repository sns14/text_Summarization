import streamlit as st
import summarize 

st.title("Text Summarization")

text_input = st.text_area("Enter your text here:")
if st.button("Summarize"):
    if text_input.strip():
        # Summarize the input text by calling the back-end logic
        try:
            summary = summarize.summarize_text(text_input)
            st.success(summary)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        #Summarize button is clicked without giving input text
        st.error("Please enter some text to summarize.")
