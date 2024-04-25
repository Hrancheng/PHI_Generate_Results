import os

from ann import remove_labels_and_compute_indices

# Function to create directories if they don't exist
def create_directories():
    if not os.path.exists('text'):
        os.makedirs('text')
    if not os.path.exists('anno'):
        os.makedirs('anno')

# Function to process files
def process_files():
    for file in os.listdir('gpt_text'):
        if file.endswith('.txt'):
            full_path = os.path.join('gpt_text', file)
            filename = os.path.basename(full_path)
            input_file = filename
            filename = os.path.splitext(filename)[0]
            output_file = f"{filename}_cleaned.txt"
            output_file_html = f"{filename}_cleaned.html"
            label_info_file = f"{filename}_ann.ann"

            # Call your ann.py script with the appropriate command-line arguments here
            remove_labels_and_compute_indices(input_file, output_file, output_file_html, label_info_file)

# Main function
def main():
    create_directories()
    process_files()

if __name__ == "__main__":
    main()
