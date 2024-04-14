import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Suppose that we have some data
text_data = "This is a sample text for Word2Vec model training with NLTK and Gensim."

stop_words = set(stopwords.words('english'))

words = word_tokenize(text_data.lower())
filtered_words = [word for word in words if word not in stop_words and word.isalnum()]

# Use Gensim to train Word2Vec model
model = Word2Vec([filtered_words], vector_size=100, window=5, min_count=1, workers=4)

# Use the model
vector = model.wv['sample']  # Get the vector of ‘sample’
similar_words = model.wv.most_similar('text')  #  find word similar to ‘sample’

print(vector)

print(similar_words)