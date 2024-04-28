import os
import re

def replace_patterns_in_files(directory):
    # List of valid categories
    B_lst = ["[B-NAME]", "[B-PHONE]", "[B-CONTACT]", "[B-ADDRESS]", "[B-LOCATION]",
             "[ETHNICITY_NATIONALITY]", "[B-DATE]", "[B-ID]", "[B-ORGANIZATION]", "[B-AGE]",
             "[B-PT_OCCUPATION]", "[B-MED_PROFESSION]"]

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                text = file.read()

            # Replace newline character with space
            text = text.replace("\n", " ")

            # Find and replace patterns
            patterns = re.findall(r"\[B-(.*?)\](.*?)\[O\]", text)
            for category, word in patterns:
                if "[B-" + category + "]" not in B_lst:
                    print(f"Invalid category found in {filename}: [B-{category}]{word}[O]")
                    text = text.replace(f"[B-{category}]{word}[O]", word)
            
            # Write modified text back to the file
            with open(filepath, 'w') as file:
                file.write(text)

# Example usage:
if __name__ == "__main__":
    directory = "gpt_text_new"  # Current directory
    replace_patterns_in_files(directory)
