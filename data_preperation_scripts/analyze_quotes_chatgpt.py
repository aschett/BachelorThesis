from openai import OpenAI
import os
from dotenv import load_dotenv
import pandas as pd

# Load OPENAI API-Key
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Load the data
file_path = '../dataset/quotes_classification_data.csv'
quotes_data = pd.read_csv(file_path)

# Function to analyze each quote using GPT-4o-Mini
def analyze_quote(quote):
    prompt = f"""
    Analyze the following quote based on the categories below. For each category, list it if the quote fits; otherwise, ignore it. Return only the relevant categories as a comma-separated list:

    Quote: "{quote}"

    Categories and Instructions:
    - Concreteness: Is the language specific and tangible, using concrete nouns or verbs?
    - Arousal: Does the quote provoke an emotional reaction or excitement?
    - Valence: Does the quote have a positive or negative emotional tone?
    - Humor: Is there any element of wit, irony, or humor in the quote?
    - Semantics: Is the quote deep, meaningful, or thought-provoking in terms of ideas or concepts?
    - Imagery: Does the quote create vivid mental images or use descriptive language?
    - Simplicity: Is the language straightforward, easy to understand, or uncomplicated?

    Return only the applicable categories, separated by commas. Do not include additional explanations or words.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

#Function that restructures the dataset to creates new columns for each of the applicable categories
def structure_dataset(dataset):
    categories = ['Concreteness', 'Arousal', 'Valence', 'Humour', 'Semantics', 'Imagery', 'Simplicity']

    # Create binary columns for each category and fill 1 if it appears and otherwise 0
    for category in categories:
        dataset[category] = dataset['Analysis'].apply(lambda x: 1 if pd.notnull(x) and category in x else 0)

    return dataset


# Add a new column for analysis that contains the number of listed applicable categories
quotes_data['Analysis'] = quotes_data['Quote'].apply(analyze_quote)

quotes_data['Category_Count'] = quotes_data['Analysis'].apply(lambda x: len(x.split(',')) if pd.notnull(x) else 0)

quotes_data = structure_dataset(quotes_data)

# Save the results to a new CSV file
try:
    quotes_data.to_csv('../ai_analyzed_dataset/quotes_analysis_results.csv', index=False)
except Exception as e:
    print("Couldn't save dataset")
    quotes_data.to_csv('./quotes_analysis_results.csv', index=False)
