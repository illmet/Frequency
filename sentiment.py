import matplotlib.pyplot as plt
from transformers import pipeline 
from wordcloud import WordCloud 
from collections import defaultdict
from processing import process_data


#get the data from the function
text = process_data()
print(text[1])

#set up the pipeline for sentiment analysis
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

#sentiments filtering
word_sentiments = defaultdict(lambda: {'POSITIVE': 0, 'NEGATIVE': 0})
#word sentiment
for excerpt in text:
    output = classifier(excerpt)
    sentiment = output[0]['label']
    for word in excerpt.split():
        word_sentiments[word][sentiment] += 1
#colouring
word_colors = {}
for word, sentiments in word_sentiments.items():
    word_colors[word] = 'green' if sentiments['POSITIVE'] >= sentiments['NEGATIVE'] else 'red'
#colour function
def color_func(word, **kwargs):
    return word_colors.get(word, 'grey')
#wordcloud
wordcloud = WordCloud(color_func=color_func, width=800, height=400).generate(' '.join(text))
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()