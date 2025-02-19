import re
import nltk
nltk.download()
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from transformers import pipeline

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

# ✅ Example usage
if __name__ == "__main__":
    text = """
    Artificial Intelligence (AI) is revolutionizing industries by automating tasks, analyzing data, 
    and improving decision-making processes. It has applications in healthcare, finance, and many other fields. 
    Machine Learning, a subset of AI, enables systems to learn from data and improve over time without being explicitly programmed.
    """
    print("Enter ur text")
    speech = input()
    
    print("\n📌 Extractive Summary:")
    print(extractive_summary(speech, num_sentences=2))

    print("\n📌 Abstractive Summary:")
    print(abstractive_summary(speech))
