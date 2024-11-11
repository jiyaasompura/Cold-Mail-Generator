import os
import tempfile

import streamlit as st
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    # Streamlit is used to create an interactive user interface
    st.title("📧 Cold Mail Generator")  # Title of the app
    cv_pdf = st.file_uploader(label='UPLOAD YOUR CV', type=['pdf'])  # File uploader for CV
    url_input = st.text_input("Enter a URL: ")  # Input field for user to enter a URL
    submit_button = st.button("Submit")  # Submit button to trigger processing

    if submit_button:
        try:
            # Load content from the provided URL
            loader = WebBaseLoader(url_input)
            data = clean_text(loader.load().pop().page_content)  # Clean the loaded data

            # Load the user's portfolio
            portfolio.load_portfolio()

            # Extract job information from the cleaned data
            jobs = llm.extract_jobs(data)
            job = jobs[0]  # Assuming we want the first job
            skills = job.get('skills', [])  # Get required skills for the job

            # Query the portfolio for relevant links based on extracted skills
            links = portfolio.query_links(skills)

            # Create a temporary file to save the uploaded CV
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(cv_pdf.read())  # Write the uploaded CV to the temp file
                tmp_file_path = tmp_file.name  # Get the name of the temporary file

            # Load and clean the uploaded CV
            pdf_loader = PyPDFLoader(tmp_file_path)
            cv_documents = pdf_loader.load()  # Load the CV documents

            if not cv_documents:
                st.error("Failed to read the uploaded CV.")  # Error handling if CV loading fails
                os.unlink(tmp_file_path)  # Clean up the temporary file
                return

            # Combine text from all pages of the PDF and clean it
            cv_text = clean_text(" ".join([doc.page_content for doc in cv_documents]))

            # Clean up the temporary file after processing
            os.unlink(tmp_file_path)

            # Generate the email content based on job details, links, and cleaned CV text
            email = llm.write_mail(job, links, cv_text)
            st.code(email, language='markdown')  # Display the generated email in markdown format
        except Exception as e:
            # Handle any exceptions that occur during processing
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    # Initialize the Chain and Portfolio objects
    chain = Chain()
    portfolio = Portfolio()

    # Set up the Streamlit page configuration
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")

    # Create the Streamlit app
    create_streamlit_app(chain, portfolio, clean_text)