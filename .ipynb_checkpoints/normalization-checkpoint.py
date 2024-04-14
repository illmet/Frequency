# Min Max Normalisation
def min_max_normalize(data):
    min_val = min(data)
    max_val = max(data)
    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
    return normalized_data

def read_values_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        words = [line.split(':')[0].strip() for line in lines]
        values = [int(line.split(':')[1].strip()) for line in lines]
    return words,values

def write_normalized_values_to_file(normalized_data, words, output_file_path):
    with open(output_file_path, 'w') as file:
        for word, value in zip(words, normalized_data):
            file.write(f'{word}: {value:.6f}\n')


def main():
    # input_file_path = 'outputs/frequency_distribution/frequency_distribution_nltk.txt'
    # output_file_path = 'outputs/Normalised/normalised_nltk.txt'

    # input_file_path = 'outputs/frequency_distribution/frequency_distribution_spacy.txt' 
    # output_file_path = 'outputs/Normalised/normalised_spacy.txt'  
   
    input_file_path = 'outputs/frequency_distribution/frequency_distribution_vanilla.txt'  
    output_file_path = 'outputs/Normalised/normalised_vanilla.txt' 
    
    
    # Read values from input file
    words,values = read_values_from_file(input_file_path)

    normalized_data = min_max_normalize(values)
    

    write_normalized_values_to_file(normalized_data, words, output_file_path)
    
    print("Normalization completed and saved to output.txt")

if __name__ == "__main__":
    main()
