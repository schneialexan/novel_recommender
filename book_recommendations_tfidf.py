import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from helper.preprocessing import makeDataset

# Load the data into a DataFrame
data = makeDataset()
# Create TF-IDF vectorizer to convert text data into numerical vectors
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(data['combined_features'])

# Compute the cosine similarity between books
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to recommend novels based on similarity
def get_recommendations(book_name, cosine_sim=cosine_sim):
    book_index = data[data['name'] == book_name].index[0]
    similar_books = list(enumerate(cosine_sim[book_index]))
    similar_books = sorted(similar_books, key=lambda x: x[1], reverse=True)
    similar_books = similar_books[1:11]  # Get the top 10 similar books
    book_indices = [x[0] for x in similar_books]
    return data['name'].iloc[book_indices]

book_name = "Reborn into Naruto World with Tenseigan"
recommendations = get_recommendations(book_name)
print(recommendations)