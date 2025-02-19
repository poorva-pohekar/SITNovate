# SITNovate
# Intelligent Document Summarization for Efficient Information Extraction

## Overview - 
This AI-powered tool generates concise summaries of lengthy documents such as research papers, legal contracts, and news articles. Using advanced NLP techniques, it extracts key information while preserving context. The system adapts to different domains, including healthcare, finance, and education.

## Features -
- Extracts text from PDF's using pdfplumber
- Extracts text from images using pytesseract(Tesseract OCR)
- Performs extractive summarization using LexRank(Sumy)
- Performs abstractive summarization using facebook/bart-large-cnn

## Installation
### Prerequisites
Ensure you have Python installed (>= 3.8).

### Install Dependencies
```bash
pip install -r requirements.txt
```
### Install Tesseract OCR (Image Processing)
#### For Ubuntu/Debian:
```bash
sudo apt install tesseract-ocr
```
#### For Arch Linux:
```bash
sudo pacman -S tesseract
```

## Dependencies
- nltk
- sumy
- transformers
- pdfplumber
- pytesseract
- Pillow    