import csv
import glob
import re

# This function extracts SpongeBob's spoken lines from a text file
def extract_spongebob_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Find all SpongeBob's lines and remove the "SpongeBob:" part
    # spongebob_lines = re.findall(r'SpongeBob: (.+)', content)
    spongebob_lines = content.split('\n')

    # Remove any text within square brackets and surrounding quotes
    cleaned_lines = []
    for line in spongebob_lines:
        line = re.sub(r'\[.*?\]', '', line)  # Remove text in square brackets
        line = line.replace('""', '')  # Remove all double quotes
        if len(line) > 2 and line:
            cleaned_lines.append(line.strip())

    return cleaned_lines

# This function processes all text files and writes the results to a CSV file
def process_files_to_csv():
    all_files = glob.glob('/home/xzrderek/cs182-project/data/SpongeBob_SquarePants_Transcripts/*.txt')  # Change the path if your text files are in a different directory
    with open('spongebob_lines1.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['SpongeBob Lines'])  # Header

        for file in all_files:
            spongebob_lines = extract_spongebob_lines(file)
            for line in spongebob_lines:
                csvwriter.writerow([line])

# Call the function to process files
process_files_to_csv()
