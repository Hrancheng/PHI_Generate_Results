import re

def remove_labels_and_compute_indices(input_file, output_file, label_info_file):
    # Define the pattern to find and remove labels
    pattern = r'\[B-(.*?)\](.*?)\[O\]'
    
    # Read the input file and remove empty lines
    with open(input_file, 'r') as file:
        lines = file.readlines()
        text = ''.join([line for line in lines if line.strip()])

    # Find all matches before removing labels
    matches = re.findall(pattern, text)

    # Remove the labels from the text and store the cleaned text
    cleaned_text = re.sub(pattern, r'\2', text)

    # Remove trailing newline characters from the cleaned text
    cleaned_text = cleaned_text.rstrip('\n')

    # Write the cleaned text to the output file
    with open(output_file, 'w') as file:
        file.write(cleaned_text)

    # Initialize a list to store the results
    results = []

    # Iterate over the matches and compute the indices in the cleaned text
    for i, (label, word) in enumerate(matches, start=1):
        # Extract the word type from the label
        word_type = label
        start_index = cleaned_text.find(word)
        end_index = start_index + len(word)
        result_str = f'T{i}\t{word_type} {start_index} {end_index}\t{word}'
        results.append(result_str)
        cleaned_text = cleaned_text.replace(word, ' ' * len(word), 1)

    # Write the label info to the label info file
    with open(label_info_file, 'w') as file:
         file.write('\n'.join(results))

    return results


def main():
    # Example usage
    input_file = 'example.txt'
    output_file = 'cleaned_example_ann.txt'
    label_info_file = 'label_info_ann.txt'
    results = remove_labels_and_compute_indices(input_file, output_file, label_info_file)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()