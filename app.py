import os
import streamlit as st
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Google Generative AI client
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("Error: GEMINI_API_KEY not found. Please set the API key in the .env file.")

def extract_text_from_excel(file):
    """
    Extracts text data from the uploaded Excel file.
    """
    df = pd.read_excel(file)
    text_data = []
    for _, row in df.iterrows():
        row_as_string = " ".join([str(item) for item in row.values if pd.notna(item)])
        text_data.append(row_as_string)
    combined_text = "\n".join(text_data)
    return combined_text

def query_gemini_api(text, question):
    """
    Queries the Google Generative AI API with the provided text and question.
    """
    try:
        prompt1 = f"Here is the data: {text}\nQuestion: {question}\nPlease provide an answer:"
        # Use the chat-based API to query the Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            contents=[prompt1]
        )
        # return response.result if response.result else "No answer provided."
        for chunk in response:
            return chunk.text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """
    Main function for the Streamlit app.
    """
    st.title("AI-Powered XLSX Q&A")
    st.write("Upload an Excel file and ask questions about its data.")

    # File upload
    uploaded_file = st.file_uploader("Upload XLSX", type=["xlsx"])

    if uploaded_file is not None:
        with st.spinner("Reading and indexing file..."):
            text = extract_text_from_excel(uploaded_file)
            st.success("File processed successfully!")

        # Question input
        question = st.text_input("Ask a question about the data:")
        if question:
            with st.spinner("Generating answer..."):
                answer = query_gemini_api(text, question)
                st.markdown(f"**Answer:** {answer}")

if __name__ == "__main__":
    main()