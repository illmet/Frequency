from matplotlib import pyplot as plt
from nltk import FreqDist

from frequency_calculation import calculate_frequency_distribution
from processing import process_data
import data
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy

def get_data():
    posts = process_data("data/posts", "content")
    comms = process_data("data/comments", "body")
    all = posts + comms
    return " ".join(all)



nltk.download('stopwords')
nltk.download('punkt')

#spaCy model to be downloaded
# !python -m spacy download en_core_web_sm

nlp = spacy.load("en_core_web_sm")

# Increase max_length to accommodate longer texts
nlp.max_length = 2000000000000

def remove_stopwords_nltk(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [w for w in word_tokens if w.lower() not in stop_words]
    return ' '.join(filtered_text)

def remove_stopwords_spacy(text):
    doc = nlp(text)
    filtered_text = [token.text for token in doc if not token.is_stop]
    return ' '.join(filtered_text)

text = get_data()

nltk_data = remove_stopwords_nltk(text)
spacy_data = remove_stopwords_spacy(text)

calculate_frequency_distribution(text, "vanilla")
calculate_frequency_distribution(nltk_data, "nltk")
calculate_frequency_distribution(spacy_data, "spacy")


