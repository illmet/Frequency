from scipy.stats import chisquare
import numpy as np
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')

def calculate_frequency_distribution(text, output_name):
    print(f"Calculating frequency distribution for {output_name}")

    # Tokenize the text
    tokenized_words = word_tokenize(text.lower())

    # Remove stopwords and punctuation
    # stop_words = set(stopwords.words('english'))
    # tokens = [word for word in tokenized_words if word.isalpha() and word not in stop_words]

    # Frequency distribution
    frequency_distribution = FreqDist(tokenized_words)

    # Get the frequencies sorted in descending order
    frequencies = sorted(frequency_distribution.values(), reverse=True)

    # Expected frequencies based on Zipf's Law
    total_words = sum(frequencies)
    expected_frequencies = [total_words / (i + 1) for i in range(len(frequencies))]

    # Scale the expected frequencies so that their sum matches the sum of the observed frequencies
    scale_factor = sum(frequencies) / sum(expected_frequencies)
    expected_frequencies = [freq * scale_factor for freq in expected_frequencies]

    # Chi-squared test
    chi_squared_statistic, p_value = chisquare(frequencies, f_exp=expected_frequencies)

    # Prepare ranks for the Zipf's law plot
    ranks = np.arange(1, len(frequencies) + 1)

    # Plot the actual frequency distribution against Zipf's Law in log scale
    plt.figure(figsize=(10, 6))
    plt.loglog(ranks, frequencies, label='Observed Frequencies', linewidth=1, color='b')
    plt.loglog(ranks, expected_frequencies, label="Expected Frequencies (Zipf's Law)", linestyle='--', color='r')

    plt.title(f'Frequency Distribution with Zipf\'s Law\nChi-squared ({output_name}): {chi_squared_statistic:.2f}, p-value: {p_value:.2g}')
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.legend()
    plt.savefig(f"outputs/plots/frequency_distribution_zipf_{output_name}.png")

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
    plt.savefig(f"outputs/plots/frequency_distribution_normal_{output_name}.png")

    # Convert the items of the frequency distribution to a list of tuples
    sorted_items = frequency_distribution.most_common()

    # Save the sorted frequency distribution to a file
    with open(f"outputs/frequency_distribution/frequency_distribution_{output_name}.txt", "w") as file:
        for word, freq in sorted_items:
            file.write(f'{word}: {freq}\n')




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
