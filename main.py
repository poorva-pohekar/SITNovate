import re
import nltk
import pytesseract
import pdfplumber
from PIL import Image
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from transformers import pipeline

# Download necessary NLTK resources
nltk.download("punkt")

# Load the pre-trained BART summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# ✅ Preprocessing: Clean text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^A-Za-z0-9.,!? ]+', '', text)  # Remove special characters
    return text.strip()

# ✅ Extractive Summarization (LexRank)
def extractive_summary(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return " ".join(str(sentence) for sentence in summary)

# ✅ Abstractive Summarization (BART)
def abstractive_summary(text):
    return summarizer(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']

# ✅ Extract text from an image (OCR)
def extract_text_from_image(image_path):
    return pytesseract.image_to_string(Image.open(image_path))

# ✅ Extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"
    return text.strip()

# ✅ Example usage
if __name__ == "__main__":
    print("Choose input type: 1. Text  2. PDF  3. Image")
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        text = input("Enter your text: ")
    elif choice == "2":
        pdf_path = input("Enter PDF file path: ")
        text = extract_text_from_pdf(pdf_path)
    elif choice == "3":
        image_path = input("Enter image file path: ")
        text = extract_text_from_image(image_path)
    else:
        print("Invalid choice")
        exit()

    text = clean_text(text)

    print("\n📌 Extractive Summary:")
    print(extractive_summary(text, num_sentences=2))

    print("\n📌 Abstractive Summary:")
    print(abstractive_summary(text))
