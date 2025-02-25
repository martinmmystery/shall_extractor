import os
import streamlit as st
import fitz  # PyMuPDF
import re
import nltk
from nltk.tokenize import sent_tokenize

# Force NLTK to download punkt if missing
nltk.data.path.append(os.path.expanduser("~") + "/nltk_data/")
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

def extract_shall_sentences(pdf_file):
    text = ""

    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text("text") + " "

    sentences = sent_tokenize(text)
    shall_sentences = [sent for sent in sentences if re.search(r'\bshall\b', sent, re.IGNORECASE)]

    return shall_sentences

# Streamlit UI
st.title("📄 PDF 'Shall' Extractor")
st.write("Upload a PDF, and I will extract sentences containing the word **'shall'**.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    sentences = extract_shall_sentences(uploaded_file)
    st.subheader("📄 Extracted Sentences:")
    for i, sentence in enumerate(sentences, 1):
        st.write(f"**{i}.** {sentence}")

    st.success("✅ Done! Scroll up to see the results.")
