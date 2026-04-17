import streamlit as st

st.title("AI Resume Screener (Basic MVP)")

resume = st.text_area("Paste Resume Text")
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if resume and job_desc:
        resume_words = set(resume.lower().split())
        job_words = set(job_desc.lower().split())

        match = resume_words.intersection(job_words)
        score = len(match) / len(job_words) * 100

        st.subheader("Results")
        st.write(f"Match Score: {score:.2f}%")
        st.write("Matched Words:", list(match)[:10])

        if score > 50:
            st.success("Selected")
        else:
            st.error("Not Selected")
