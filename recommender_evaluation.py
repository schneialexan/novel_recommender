import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from helper.preprocessing import makeDataset

def content_based_recommendation(book_name, cosine_sim, top_n=10):
    # Get the index of the book
    book_index = data[data['name'] == book_name].index[0]

    # Calculate the cosine similarity between the specified book and all other books
    similar_books = list(enumerate(cosine_sim[book_index]))

    # Sort the similar books by similarity score in descending order
    similar_books = sorted(similar_books, key=lambda x: x[1], reverse=True)

    # Get the top N similar books
    book_indices = [x[0] for x in similar_books[1:top_n + 1]]
    
    # Return the names of the top N similar books
    return data['name'].iloc[book_indices]

if __name__ == '__main__':
    data = makeDataset()
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(data['combined_features'])

    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

    top_n = 10
    correct_predictions = 0

    for book_name in test_data['name'].unique():
        # Generate content-based recommendations for the current book using the recommendation function
        content_recommendations = content_based_recommendation(book_name, cosine_sim, top_n)
        # Create the ground truth by finding all other books in the testing dataset
        true_next_books = test_data[test_data['name'] != book_name]['name'].tolist()
        true_next_books = set(true_next_books)
        # Convert the recommendations and ground truth to sets for easy comparison
        content_recommendations = set(content_recommendations[:top_n])
        # Check if there are common books between the recommendations and the expected next books
        common_books = content_recommendations.intersection(true_next_books)
        # If at least one book matches, it's considered a correct prediction, so increment the correct_predictions count
        if len(common_books) > 0:
            correct_predictions += 1
    # Accuracy = (Number of Correct Predictions) / (Total Number of Unique Book Names in the Testing Dataset)
    accuracy = correct_predictions / len(test_data['name'].unique())
    print(f"Top-{top_n} Accuracy for Content-Based Recommendation: {accuracy}")
