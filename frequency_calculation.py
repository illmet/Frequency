import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

import nltk
nltk.download('punkt')
nltk.download('stopwords')

sample_text = """Natural Language Processing is fascinating.
It allows computers to understand human language.
This tutorial is about frequency distribution using NLTK.Frequency distribution in text processing refers to the 
representation of how often different terms (usually words or tokens) appear within a given text or a corpus. 
In other words, it is a statistical measure used to describe the occurrence of each term in the text.
"""

# Tokenize the text
tokenized_words = word_tokenize(sample_text.lower())
print(tokenized_words)

# Fetch the stop words
stop_words = set(stopwords.words('english'))
stop_words = stop_words.union({',', '.', '(', ')'})  # Remove stop words
filtered_words = [word for word in tokenized_words if word.lower() not in stop_words]

# Frequency distribution
frequency_distribution = FreqDist(filtered_words)
print(frequency_distribution)

# Display the most common words
print(frequency_distribution.most_common(10))

# Visualizing Frequency Distribution
# visualise top 10
frequency_distribution.plot(10, cumulative=False)
plt.show()
