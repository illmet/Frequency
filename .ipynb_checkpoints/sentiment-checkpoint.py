import matplotlib.pyplot as plt
from transformers import pipeline 
from wordcloud import WordCloud 
from collections import defaultdict
from processing import process_data

#set up the pipeline for sentiment analysis
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

#printing out the sentiment analysis of all posts' content:
def sentiment_analysis(text):
    aggregated = []
    for i in range(len(text)):
        output = classifier(text[i])
        #check for negative/positive sentiment
        if output[0]['label'] == 'POSITIVE':
            aggregated.append(output[0]['score'])
        else:
            aggregated.append(-output[0]['score'])
        print(f"Post {i+1}, sentiment: {output[0]['label']}, score: {output[0]['score']:.5f}")
    return aggregated

#for debugging
#g = sentiment_analysis(posts)
#print(sum(g)/len(g))

#visualisation for the sentiment analysis
def visualise_sentiments(text):
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