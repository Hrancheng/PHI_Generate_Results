#!/bin/bash

# Define the folder path
folder_path="."

# Navigate to the folder
cd "$folder_path" || exit

# Iterate over each file in the folder
for file in output_*.txt; do
    # Extract the index from the file name
    index=$(echo "$file" | grep -oP '\d+(?=\.txt)')

    # Calculate the new index
    new_index=$((index + 377))

    # Generate the new file name
    new_file="note_${new_index}.txt"

    # Rename the file
    mv "$file" "$new_file"

    echo "Renamed $file to $new_file"
done
