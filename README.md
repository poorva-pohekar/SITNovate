# SITNovate
# Intelligent Document Summarization for Efficient Information Extraction

## Overview - 
This AI-powered tool generates concise summaries of lengthy documents such as research papers, legal contracts, and news articles. Using advanced NLP techniques, it extracts key information while preserving context. The system adapts to different domains, including healthcare, finance, and education.

## Features -
- Extracts text from PDF's using pdfplumber
- Extracts text from images using pytesseract(Tesseract OCR)
- Performs extractive summarization using LexRank(Sumy)
- Performs abstractive summarization using facebook/bart-large-cnn

## Requirements
- Install Tesseract OCR(Image Processing)
    For ubuntu/Debian:
    sudo apt install tesseract-ocr
    For Arch Linux:
    sudo pacman -S tesseract

## Dependencies
- nltk
- sumy
- transformers
- pdfplumber
- pytesseract
- Pillow    