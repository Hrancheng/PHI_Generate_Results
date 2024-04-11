import re

def remove_labels_and_compute_indices(input_file, output_file, output_file_html, label_info_file):
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

    ########### ADDED: HTML FORMAT TO HIGHLIGHT KEY PHRASES ###############

    cleaned_text_copy = cleaned_text

    # Read the input file and remove empty lines
    with open(input_file, 'r') as file:
        lines = file.readlines()
        text = ''.join([line for line in lines if line.strip()])

    # Find all matches before removing labels
    matches = re.findall(pattern, text)

    # Initialize cleaned HTML text
    cleaned_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cleaned Text</title>
    </head>
    <body>
    """

    # Counter for word indices
    index = 1

    # Iterate over the matches and compute the indices in the cleaned text
    for label, word in matches:
        # Extract the word type from the label
        word_type = label
        start_index = cleaned_text_copy.find(word)
        end_index = start_index + len(word)
        
        # Generate HTML for the word with red color and superscript index
        word_html = f'<span style="color:red">{word}<sup>{index}</sup></span>'
        
        # Replace the word in the cleaned_html with the styled version
        cleaned_html += cleaned_text_copy[:start_index] + word_html
        cleaned_text_copy = cleaned_text_copy[end_index:]
        
        # Increment index for the next word
        index += 1

    # Append any remaining text to cleaned_html
    cleaned_html += cleaned_text_copy

    cleaned_html += """
    </body>
    </html>
    """

    # Write the cleaned HTML text to the output file
    with open(output_file_html, 'w') as file:
        file.write(cleaned_html)
    
    #######################################################################

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
    output_file_html = 'cleaned_example_ann.html'
    label_info_file = 'label_info_ann.txt'
    results = remove_labels_and_compute_indices(input_file, output_file, output_file_html, label_info_file)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()