import streamlit as st
import PyPDF2
from resume_agent import summarize, generate_cover_letter

st.set_page_config(page_title="CV Tailor Agent")

st.title("📄 CV Tailor Agent")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
job_description = st.text_area("Paste the job description here")

if uploaded_file and job_description:
    with st.spinner("Reading resume..."):
        reader = PyPDF2.PdfReader(uploaded_file)
        resume_text = "\n".join([page.extract_text() for page in reader.pages])

    st.subheader("Resume Summary")
    summary = summarize(resume_text)
    st.write(summary)

    st.subheader("Cover Letter")
    cover_letter = generate_cover_letter(resume_text, job_description)
    st.write(cover_letter)

    st.download_button("📥 Download Cover Letter", data=cover_letter, file_name="cover_letter.txt")

