import csv

# Processes the input file to extract memorable and non-memorable quotes.
def process_file(input_file_path):
    try:
        with open(input_file_path, 'r', encoding='utf-8', errors='replace') as file:
            lines = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file {input_file_path} was not found.")
        return []
    except Exception as e:
        print(f"Error reading {input_file_path}: {e}")
        return []

    quotes = []
    
    for i in range(0, len(lines), 4):
        memorable_quote = lines[i+1]
        non_memorable_quote = ' '.join(lines[i+3].split()[1:])  # The join is needed to get rid of the leading number in the ".txt" file
                
        # Append quotes to the list with their corresponding types
        quotes.append((memorable_quote, "Yes"))
        quotes.append((non_memorable_quote, "No"))

    return quotes

def write_to_csv(quotes, csv_file_path):
    try:
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Quote', 'Memorable'])
            
            # Write each quote and its type to the CSV file
            for quote, quote_type in quotes:
                writer.writerow([quote, quote_type])
    except Exception as e:
        print(f"Error writing to {csv_file_path}: {e}")

if __name__ == "__main__":
    input_file_path = './moviequotes.memorable_nonmemorable_pairs.txt'
    csv_file_path = './quotes_classification_data.csv'

    quotes = process_file(input_file_path)
    if quotes:
        write_to_csv(quotes, csv_file_path)
