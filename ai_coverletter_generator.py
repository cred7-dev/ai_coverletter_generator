import streamlit as st
import google.genai as genai

google_api_key = st.secrets["google"]["api_key"]
c = genai.Client(api_key=google_api_key)

st.title("AI Cover Letter Generator")

Job_title = st.text_input("Enter Job Title:")
Summary = st.text_input("Enter Resume Summary")

if st.button("Generate Cover Letter"):
    prompt = f"Write a cover letter for {Job_title} using these resume points: {Summary}"
    response = c.models.generate_content(model = "gemini-3.5-flash", contents = prompt)
    st.write(response.text)