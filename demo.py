import streamlit as st
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def main():
    st.title("Resume Job Description Matcher")

    st.sidebar.title("Upload Files")
    job_desc = st.sidebar.text_area("Upload Job Description")
    resume_file = st.sidebar.file_uploader("Upload Resume (DOCX)", type="docx")

    if job_desc and resume_file:
        job_des = job_desc # extract the data from job description doc
        resume = docx2txt.process(resume_file) # extract the data from resume doc

        # Combine job description and resume text
        content = [job_des, resume]

        # Vectorize the text
        cv = CountVectorizer()
        matrix = cv.fit_transform(content)

        # Calculate cosine similarity
        similarity_matrix = cosine_similarity(matrix)

        # Display similarity percentage
        match_percent = similarity_matrix[1][0] * 100
        st.write(f'Resume matches by: {match_percent:.2f} %')

if __name__ == "__main__":
    main()
