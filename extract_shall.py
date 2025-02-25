# -*- coding: utf-8 -*-
import fitz  # PyMuPDF
import re
import nltk
nltk.download('punkt')  # Download sentence tokenizer
nltk.download('punkt_tab')  # Try downloading punkt_tab if needed

from nltk.tokenize import sent_tokenize

def extract_shall_sentences(pdf_path):
    text = ""

    # Open the PDF and extract text
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text") + " "

    # Tokenize into sentences
    sentences = sent_tokenize(text)

    # Extract sentences containing the word "shall"
    shall_sentences = [sent for sent in sentences if re.search(r'\bshall\b', sent, re.IGNORECASE)]

    return shall_sentences

if __name__ == "__main__":
    # Example usage
    pdf_file_path = "G-c-PCR-023 Railway infrastructure (v2024-04-30).pdf"  # Replace with your PDF file path
    sentences_with_shall = extract_shall_sentences(pdf_file_path)

    # Print or save results
    for i, sentence in enumerate(sentences_with_shall, 1):
        print(f"{i}. {sentence}")
