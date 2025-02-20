import streamlit as st
import re
import nltk
import pytesseract
import pdfplumber
from PIL import Image
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from transformers import pipeline

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)  # Use CPU


# Download necessary NLTK resources
nltk.download("punkt")

# Load the pre-trained BART summarization model
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Preprocessing: Clean text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^A-Za-z0-9.,!? ]+', '', text)  # Remove special characters
    return text.strip()

# Extractive Summarization (LexRank)
def extractive_summary(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return " ".join(str(sentence) for sentence in summary)

# Abstractive Summarization (BART)
def abstractive_summary(text):
    return summarizer(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']

# Extract text from an image (OCR)
def extract_text_from_image(image):
    return pytesseract.image_to_string(image)

# Extract text from a PDF
def extract_text_from_pdf(pdf):
    text = ""
    with pdfplumber.open(pdf) as pdf_file:
        for page in pdf_file.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"
    return text.strip()


# Streamlit UI Configuration
st.set_page_config(page_title="Ninja Summarizer", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            color: #ff5733;
        }
        .sub-title {
            text-align: center;
            font-size: 1.5rem;
            color: #FFFFFF;
        }
        .summary-box {
            background-color: #f0f2f6;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Page Header
st.markdown("<h1 class='main-title'>🤖 Ninja Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>AI-Powered Document Summarization by Team Neural Network Ninjas 🚀</h3>", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("⚡ Choose an input type")
option = st.sidebar.radio("Select Input Type:", ["Text", "PDF", "Image"], index=0)
st.sidebar.markdown("---")
st.sidebar.info("This tool extracts and summarizes text from PDFs, images, and plain text using advanced AI models.")

# Main Layout
col1, col2 = st.columns([2, 3])

if option == "Text":
    with col1:
        user_text = st.text_area("✍️ Enter your text:")
        summarize_button = st.button("Summarize")
    
    if summarize_button and user_text:
        with st.spinner("Processing..."):
            cleaned_text = clean_text(user_text)
            extractive = extractive_summary(cleaned_text)
            abstractive = abstractive_summary(cleaned_text)
        
        with col2:
            st.subheader("📌 Extractive Summary")
            st.success(extractive)
            st.subheader("📌 Abstractive Summary")
            st.info(abstractive)

elif option == "PDF":
    with col1:
        uploaded_pdf = st.file_uploader("📂 Upload a PDF", type=["pdf"])
    
    if uploaded_pdf and st.button("Summarize PDF"):
        with st.spinner("Extracting text from PDF..."):
            extracted_text = extract_text_from_pdf(uploaded_pdf)
            cleaned_text = clean_text(extracted_text)
            extractive = extractive_summary(cleaned_text)
            abstractive = abstractive_summary(cleaned_text)
        
        with col2:
            st.subheader("📌 Extractive Summary")
            st.success(extractive)
            st.subheader("📌 Abstractive Summary")
            st.info(abstractive)

elif option == "Image":
    with col1:
        uploaded_image = st.file_uploader("📷 Upload an Image", type=["png", "jpg", "jpeg"])
    
    if uploaded_image and st.button("Summarize Image"):
        with st.spinner("Extracting text from Image..."):
            extracted_text = extract_text_from_image(Image.open(uploaded_image))
            cleaned_text = clean_text(extracted_text)
            extractive = extractive_summary(cleaned_text)
            abstractive = abstractive_summary(cleaned_text)
        
        with col2:
            st.subheader("📌 Extractive Summary")
            st.success(extractive)
            st.subheader("📌 Abstractive Summary")
            st.info(abstractive)

st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 Developed by Neural Network Ninjas")
