import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load the book dataset (replace 'novels_data.csv' with your actual dataset)
data = pd.read_csv('data/novels_0.1.3.csv')

# Fill missing values
data = data.fillna('')

data['authors'] = data['authors'].str.strip("[]").str.replace("'", "").str.split(', ')
data['genres'] = data['genres'].str.strip("[]").str.replace("'", "").str.split(', ')
data['tags'] = data['tags'].str.strip("[]").str.replace("'", "").str.split(', ')
data['original_language'] = data['original_language'].str.replace("'", "")
data['rating'] = data['rating'].astype(float)


data['combined_features'] = data['name'] + ' ' + data['authors'].apply(lambda x: ' '.join(x)) + ' ' + data['genres'].apply(lambda x: ' '.join(x)) + ' ' + data['tags'].apply(lambda x: ' '.join(x))

# Define a TF-IDF vectorizer for text attributes (genres, tags, and authors)
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Create a TF-IDF matrix for text attributes
tfidf_matrix = tfidf_vectorizer.fit_transform(data['combined_features'])

# Compute the cosine similarity between books based on the TF-IDF matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Define a function to get book recommendations for a given user based on their reading history
def get_user_recommendations(user, user_history, data, cosine_sim, top_n=5):
    if user not in user_history:
        return "User not found in the user history."
    
    user_books = user_history[user]
    
    # Create an empty array to store the sum of cosine similarity scores
    sum_sim_scores = [0] * len(data)

    # Calculate the sum of cosine similarity scores for each book the user has read
    for book in user_books:
        if book in data['name'].values:
            book_idx = data[data['name'] == book].index[0]
            sim_scores = cosine_sim[book_idx]
            sum_sim_scores = [sum(x) for x in zip(sum_sim_scores, sim_scores)]

    # Combine the book indices with their corresponding sum scores
    book_scores = list(enumerate(sum_sim_scores))

    # Sort the books based on the sum of similarity scores
    book_scores = sorted(book_scores, key=lambda x: x[1], reverse=True)

    # Get the top N recommended books
    book_indices = [i[0] for i in book_scores[:top_n]]

    # Return the top N recommended books
    return data['name'].iloc[book_indices]

# Create a fake user history (replace with actual user history)
user_history = {
    'User1': ["A Former Child Soldier Who Uses a Magic Sword Wants to Live with an Older Sister of a Former Enemy Executive",
              "A Lifelong Love Affair At Work"],
    'User2': ["A Saint Who Was Adopted by the Grand Duke"]
}

# Get recommendations for a specific user (e.g., 'User1')
user_to_recommend = 'User1'
recommendations = get_user_recommendations(user_to_recommend, user_history, data, cosine_sim)

# Print the recommended books for the user
print(f"Recommended books for {user_to_recommend}: \n{recommendations}")