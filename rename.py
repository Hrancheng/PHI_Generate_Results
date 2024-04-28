import os
import shutil
import re

# Define directories
ann_directory = "./anno_new/"
txt_directory = "./text_new/"

# Get list of .ann files
ann_files = [f for f in os.listdir(ann_directory) if f.endswith(".ann")]

# Get list of .txt files
txt_files = [f for f in os.listdir(txt_directory) if f.endswith(".txt")]

# Function to remove non-numeric characters from filename (except for extension)
def clean_filename(filename):
    name, ext = os.path.splitext(filename)
    name = re.sub(r'\D', '', name)  # Remove all non-numeric characters
    return f"{name}{ext}"

# Iterate through .ann files
for ann_file in ann_files:
    # Define new filename for .ann file
    new_ann_filename = clean_filename(ann_file)
    
    # Copy and rename .ann file
    shutil.copyfile(os.path.join(ann_directory, ann_file), os.path.join(ann_directory, new_ann_filename))
    
    # Remove old .ann file
    os.remove(os.path.join(ann_directory, ann_file))

# Iterate through .txt files
for txt_file in txt_files:
    # Define new filename for .txt file
    new_txt_filename = clean_filename(txt_file)
    
    # Copy and rename .txt file
    shutil.copyfile(os.path.join(txt_directory, txt_file), os.path.join(txt_directory, new_txt_filename))
    
    # Remove old .txt file
    os.remove(os.path.join(txt_directory, txt_file))

print("Conversion completed successfully!")


