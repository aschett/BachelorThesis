import pandas as pd

# List of file paths and memorable labels
file_paths = {
    '../generated_datasets/memorable_concreteness.csv': 1,
    '../generated_datasets/memorable_emotional.csv': 1,
    '../generated_datasets/memorable_imagery.csv': 1,
    '../generated_datasets/memorable_valence.csv': 1,
    '../generated_datasets/non_memorable_texts.csv': 0
}

# Empty list to hold the dataframes
dfs = []


for file, memorable_value in file_paths.items():
    try:
        df = pd.read_csv(file)

        df['Memorable'] = memorable_value
        dfs.append(df)
    
    except FileNotFoundError:
        print(f"Error: File {file} not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: File {file} is empty.")
    except pd.errors.ParserError:
        print(f"Error: File {file} could not be parsed.")
    except Exception as e:
        print(f"An unexpected error occurred while processing {file}: {e}")


merged_df = pd.concat(dfs, ignore_index=True)

try:
    merged_df.to_csv('../generated_datasets/merged_dataset.csv', index=False)
    print("Merged dataset saved.")
except Exception as e:
    print(f"Error saving the merged dataframe: {e}")
