import streamlit as st
from botG import query

st.title("Bot G(Powered by Google)")

question = st.text_input(label="Question:", placeholder="Ask me anything general")

if question:
    response = query(question)

    st.header("Here's what I found...")
    st.write(response)