import numpy as np
from sklearn.cluster import KMeans
import json
from matplotlib import pyplot as plt

# Choose the number of clusters
num_clusters = 12

# Example dictionaries (replace with your actual data)
with open('data/frequency.json', 'r') as f:
    frequency = json.load(f)
with open('data/importance.json', 'r') as f:
    importance = json.load(f)

# extract words exist in both dictionaries
words = list(set(frequency.keys()) & set(importance.keys()))

print(f'Number of words: {len(words)}')

# show the words missed in the importance dictionary
missed_words = set(frequency.keys()) - set(importance.keys())
with open('data/missed_words.json_freq', 'w') as f:
    json.dump(list(missed_words), f, indent=1)

# show the words missed in the frequency dictionary
missed_words = set(importance.keys()) - set(frequency.keys())
with open('data/missed_words.json_imp', 'w') as f:
    json.dump(list(missed_words), f, indent=1)

exit(1)

features = np.array([(frequency[word], importance[word]) for word in words])

# visualize the data
plt.figure(figsize=(8, 6))
plt.scatter(features[:, 0], features[:, 1], s=10, c='b', marker='o')
plt.xlabel('Frequency')
plt.ylabel('Importance')
plt.title('Word Clustering')
plt.grid()
plt.show()



# Run K-Means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(features)
clusters = kmeans.labels_

# Visualize the clusters
plt.figure(figsize=(8, 6))
plt.scatter(features[:, 0], features[:, 1], c=clusters, s=10, cmap='viridis')
plt.xlabel('Frequency')
plt.ylabel('Importance')
plt.title('Word Clustering')
plt.grid()
plt.show()


# print the quality of each cluster
for i in range(num_clusters):
    cluster_words = [words[j] for j in range(len(words)) if clusters[j] == i]
    cluster_importances = [importance[word] for word in cluster_words]
    average_importance = sum(cluster_importances) / len(cluster_importances) if cluster_importances else 0
    cluster_frequencies = [frequency[word] for word in cluster_words]
    average_frequency = sum(cluster_frequencies) / len(cluster_frequencies) if cluster_frequencies else 0
    print(f'Cluster {i + 1} ({len(cluster_words)} words, average importance: {average_importance}, average frequency: {average_frequency})\n'
          f'{cluster_words}\n')
