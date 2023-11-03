import pandas as pd

def makeDataset(path='novels_0.1.3.csv'):
    # Load the data into a DataFrame
    data = pd.read_csv(path)

    # Fill missing values
    data = data.fillna('')
    # Preprocess the data
    data['authors'] = data['authors'].str.strip("[]").str.replace("'", "").str.split(', ')
    data['genres'] = data['genres'].str.strip("[]").str.replace("'", "").str.split(', ')
    data['tags'] = data['tags'].str.strip("[]").str.replace("'", "").str.split(', ')
    data['original_language'] = data['original_language'].str.replace("'", "")
    data['rating'] = data['rating'].astype(float)


    data['combined_features'] = data['name'] + ' ' + data['authors'].apply(lambda x: ' '.join(x)) + ' ' + data['genres'].apply(lambda x: ' '.join(x)) + ' ' + data['tags'].apply(lambda x: ' '.join(x))
    return data
