import nltk
import numpy as np
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')
nltk.download('stopwords')


def calculate_frequency_distribution(text, output_name):
    print(f"Calculating frequency distribution for {output_name}")

    # Tokenize the text
    tokenized_words = word_tokenize(text.lower())

    # Frequency distribution
    frequency_distribution = FreqDist(tokenized_words)

    # Get the frequencies sorted in descending order
    frequencies = sorted(frequency_distribution.values(), reverse=True)

    # Prepare ranks for the Zipf's law plot
    ranks = np.arange(1, len(frequencies) + 1)

    # Plot the actual frequency distribution against power law in normal scale
    plt.figure(figsize=(10, 6))
    plt.plot(frequencies, label=f'{output_name}', linewidth=1, color='b')

    # Plot a power law distribution curve
    power_law = [frequencies[0] * (float(rank) ** (-1)) for rank in ranks]

    plt.plot(ranks, power_law, label='Power Law', linestyle='--', color='g')

    plt.title('Frequency Distribution with Power Law')
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.legend()
    plt.savefig(f"outputs/frequency_distribution_normal_{output_name}.png")

    # Now plot the actual frequency distribution against Zipf's law in log scale
    plt.figure(figsize=(10, 6))
    plt.loglog(frequencies, label=f'{output_name}', linewidth=1, color='b')

    # Generate and plot the Zipf curve
    zipf_dist = [frequencies[0] / rank for rank in ranks]  # Zipf's law
    plt.loglog(ranks, zipf_dist, label="Zipf's Law", linestyle='--', color='r')

    plt.title('Frequency Distribution with Zipf\'s Law')
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.legend()
    plt.savefig(f"outputs/frequency_distribution_log_{output_name}.png")

    # Save the frequency distribution to a file
    with open(f"outputs/frequency_distribution_{output_name}.txt", "w") as file:
        for rank, freq in zip(ranks, frequencies):
            file.write(f'Rank: {rank}, Frequency: {freq}\n')



if __name__ == '__main__':

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
