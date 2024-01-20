import os
import shutil
import pandas as pd


# Step 1: Read names from the text file into a set
txt_file_path = 'namad.txt'

with open(txt_file_path, 'r') as file:
    extracted_set = set()

    for text in file:
        # Split the text by '(' and take the first part
        parts = text.split('(')
        extracted_text = parts[0].strip()
        extracted_set.add(extracted_text)

# Step 2: List files in the folder
folder_path = './all_csv'
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Step 3: Create a new folder
new_folder_path = './matched_files'
os.makedirs(new_folder_path, exist_ok=True)

# Step 4: Move matching files to the new folder
for csv_file in csv_files:
    # Extract the file name without the extension
    file_name = os.path.splitext(csv_file)[0]

    # Check if the file name is in the extracted_set
    if file_name in extracted_set:
        # Build the full paths for source and destination
        source_path = os.path.join(folder_path, csv_file)
        destination_path = os.path.join(new_folder_path, csv_file)

        # Move the file to the new folder
        shutil.copy(source_path, destination_path)

# Specify the directory containing your CSV files
new_directory = './matched_files'



# Get a list of all CSV files in the directory
csv_files = [file for file in os.listdir(new_directory) if file.endswith('.csv')]

# Initialize an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Loop through each CSV file and merge its data into the main DataFrame
for csv_file in csv_files:
    file_path = os.path.join(new_directory, csv_file)
    # Detect the encoding
    # encoding = detect_encoding(file_path)
    df = pd.read_csv(file_path, encoding='utf-8')
    merged_data = pd.concat([merged_data, df], ignore_index=True)

# Save the merged data to a new CSV file
merge_path = './merge_out'
os.makedirs(merge_path, exist_ok=True)
merged_data.to_csv('./merge_out/merged_data.csv', index=False)