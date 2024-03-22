from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
example_sent = """This is a sample sentence,
                  showing off the stop words filtration."""
 
stop_words = set(stopwords.words('english'))
 
word_tokens = word_tokenize(example_sent)
# converts the words in word_tokens to lower case and then checks whether
#they are present in stop_words or not
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
#with no lower case conversion
filtered_sentence = []
 
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
 
print(word_tokens)
print(filtered_sentence)

#Random website https://www.smartdatacollective.com/social-media-analytics-stop-words/

import spacy 

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")
 
# Sample text
text = "There is a pen on the table"
 
# Process the text using spaCy
doc = nlp(text)
 
# Remove stopwords
filtered_words = [token.text for token in doc if not token.is_stop]
 
# Join the filtered words to form a clean text
clean_text = ' '.join(filtered_words)
 
print("Original Text:", text)
print("Text after Stopword Removal:", clean_text)

