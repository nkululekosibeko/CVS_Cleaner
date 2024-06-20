import csv

# Read the CSV file as raw text
file_path = r'C:\Users\ell8n\OneDrive - Durban University of Technology\ell8•One\James Farming (PTY) Ltd. (Innobiz)\Site\exone.csv'  # Update with your file path
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Find the header line and determine the correct number of columns
header = lines[0].strip().split(',')
num_columns = len(header)

# Initialize a list to store the cleaned rows
cleaned_rows = [header]

# Process each line to ensure it has the correct number of columns
for line in lines[1:]:
    # Split the line into fields
    fields = line.strip().split(',')

    # If the number of fields is incorrect, try to fix it
    if len(fields) != num_columns:
        # Example fix: Join extra fields or add missing fields
        while len(fields) > num_columns:
            fields[-2] = fields[-2] + ',' + fields[-1]
            fields.pop()
        while len(fields) < num_columns:
            fields.append('')

    # Add the cleaned row to the list
    cleaned_rows.append(fields)

# Save the cleaned data to a new CSV file
cleaned_file_path = 'cleaned_exone.csv'  # Update with your desired output file path
try:
    with open(cleaned_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(cleaned_rows)
    print(f'Cleaned file saved to {cleaned_file_path}')
except Exception as e:
    print(f"An error occurred while saving the file: {e}")
