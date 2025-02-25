# main.py
import tkinter as tk
from tkinter import filedialog
import extract_shall  # import your unchanged code

def main():
    # Hide that default Tk window
    root = tk.Tk()
    root.withdraw()

    # Ask the user to pick a PDF
    print("Please select a PDF file...")
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if not pdf_path:
        print("No file selected. Exiting...")
        return

    # Call the function from your original code
    sentences_with_shall = extract_shall.extract_shall_sentences(pdf_path)

    # Print results
    print("\nFound the following 'shall' sentences:\n")
    for i, sentence in enumerate(sentences_with_shall, 1):
        print(f"{i}. {sentence}")

if __name__ == "__main__":
    main()
