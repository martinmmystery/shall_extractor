import streamlit as st
import fitz  # PyMuPDF
import re
import nltk
from nltk.tokenize import sent_tokenize

# Force-download necessary NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')

def extract_shall_sentences(pdf_file):
    text = ""
    # Read the PDF from the uploaded file
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text("text") + " "
    # Tokenize text into sentences and filter for those containing "shall"
    sentences = sent_tokenize(text)
    shall_sentences = [sent for sent in sentences if re.search(r'\bshall\b', sent, re.IGNORECASE)]
    return shall_sentences

# Streamlit UI
st.title("📄 PDF 'Shall' Extractor")
st.write("Upload a PDF, and I'll extract all sentences containing the word **'shall'**.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    sentences = extract_shall_sentences(uploaded_file)
    st.subheader("Extracted Sentences:")
    if sentences:
        for i, sentence in enumerate(sentences, 1):
            st.write(f"**{i}.** {sentence}")
    else:
        st.write("No sentences containing 'shall' were found.")
    st.success("Done!")
