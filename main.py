import os
import streamlit as st
import fitz  # PyMuPDF
import re
import nltk
from nltk.tokenize import sent_tokenize

# Define a custom directory for NLTK data (inside your project directory)
NLTK_DATA_PATH = os.path.join(os.path.dirname(__file__), "nltk_data")
os.makedirs(NLTK_DATA_PATH, exist_ok=True)

# Set the NLTK_DATA environment variable so NLTK looks there first
os.environ["NLTK_DATA"] = NLTK_DATA_PATH
nltk.data.path.append(NLTK_DATA_PATH)

# Force-download the necessary NLTK resources to the specified directory
nltk.download("punkt", download_dir=NLTK_DATA_PATH)
nltk.download("punkt_tab", download_dir=NLTK_DATA_PATH)

def extract_shall_sentences(pdf_file):
    text = ""
    # Read the PDF content from the uploaded file
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text("text") + " "
    # Tokenize text into sentences and filter those containing "shall"
    sentences = sent_tokenize(text)
    shall_sentences = [sent for sent in sentences if re.search(r'\bshall\b', sent, re.IGNORECASE)]
    return shall_sentences

# Streamlit UI
st.title("📄 PDF 'Shall' Extractor")
st.write("Upload a PDF, and I'll extract all sentences containing the word **'shall'**.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    sentences = extract_shall_sentences(uploaded_file)
    st.subheader("📄 Extracted Sentences:")
    if sentences:
        for i, sentence in enumerate(sentences, 1):
            st.write(f"**{i}.** {sentence}")
    else:
        st.write("No sentences containing 'shall' were found.")
    st.success("✅ Done!")
