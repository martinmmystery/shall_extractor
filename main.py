import streamlit as st
import fitz  # PyMuPDF
import re
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def extract_shall_sentences(pdf_file):
    text = ""

    # Open the PDF and extract text
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text("text") + " "

    # Tokenize into sentences
    sentences = sent_tokenize(text)

    # Extract sentences containing the word "shall"
    shall_sentences = [sent for sent in sentences if re.search(r'\bshall\b', sent, re.IGNORECASE)]

    return shall_sentences

# Streamlit UI
st.title("📄 PDF Shall Extractor")
st.write("Upload a PDF, and this app will extract all sentences containing 'shall'.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    sentences = extract_shall_sentences(uploaded_file)
    
    if sentences:
        st.subheader("Sentences containing 'shall':")
        for i, sentence in enumerate(sentences, 1):
            st.write(f"{i}. {sentence}")
    else:
        st.write("No sentences containing 'shall' found.")
