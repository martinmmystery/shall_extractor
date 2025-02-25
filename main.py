import streamlit as st
import fitz  # PyMuPDF
import re
import nltk
from nltk.tokenize import sent_tokenize

# Download necessary NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")

def extract_shall_sentences(pdf_file):
    text = ""
    # Open the PDF and extract text
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text("text") + " "
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    # Filter sentences containing 'shall'
    shall_sentences = [sentence for sentence in sentences if re.search(r'\bshall\b', sentence, re.IGNORECASE)]
    return shall_sentences

# Streamlit UI
st.title("PDF 'Shall' Extractor with Checkboxes")
st.write("Upload a PDF and review each sentence containing 'shall'. Tick the box if the condition is satisfied.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    sentences = extract_shall_sentences(uploaded_file)
    if sentences:
        st.write(f"Found {len(sentences)} sentences containing 'shall'. Please review below:")
        results = {}
        for i, sentence in enumerate(sentences):
            # Create a checkbox for each sentence
            is_checked = st.checkbox(f"Sentence {i+1}: {sentence}", key=f"checkbox_{i}")
            results[sentence] = is_checked
        st.write("### Review Results:")
        for sentence, satisfied in results.items():
            st.write(f"**{'Satisfied' if satisfied else 'Not Satisfied'}:** {sentence}")
    else:
        st.write("No sentences containing 'shall' were found.")
