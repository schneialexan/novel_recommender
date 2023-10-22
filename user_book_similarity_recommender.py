import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('data/novels_0.1.3.csv')

# Fill missing values
data = data.fillna('')
data['authors'] = data['authors'].str.strip("[]").str.replace("'", "").str.split(', ')
data['genres'] = data['genres'].str.strip("[]").str.replace("'", "").str.split(', ')
data['tags'] = data['tags'].str.strip("[]").str.replace("'", "").str.split(', ')
data['original_language'] = data['original_language'].str.replace("'", "")
data['rating'] = data['rating'].astype(float)


data['combined_features'] = data['name'] + ' ' + data['authors'].apply(lambda x: ' '.join(x)) + ' ' + data['genres'].apply(lambda x: ' '.join(x)) + ' ' + data['tags'].apply(lambda x: ' '.join(x))

# Create a user-book interaction matrix (replace with actual user data if available)
# Rows represent users, columns represent books, and values represent user ratings
# For simplicity, I'll use a random matrix in this example
user_data = {
    'User1': [4.0, 0, 3.0, 0, 0],
    'User2': [0, 0, 5.0, 4.0, 0],
    'User3': [0, 0, 0, 4.5, 5.0],
    'User4': [3.0, 4.0, 0, 0, 0],
    'User5': [0, 0, 4.0, 3.5, 4.0]
}

user_ratings_df = pd.DataFrame(user_data)
user_book_matrix = user_ratings_df.transpose()

# Standardize user ratings (z-scores)
scaler = StandardScaler()
user_book_matrix_scaled = scaler.fit_transform(user_book_matrix)

user_similarity = cosine_similarity(user_book_matrix)

def get_user_based_recommendations(user_id, user_similarity, user_book_matrix, data, top_n=5):
    user_index = user_ratings_df.columns.get_loc(user_id)

    # Get the most similar users to the target user
    similar_users = sorted(range(len(user_similarity[user_index])), key=lambda i: user_similarity[user_index][i], reverse=True)

    # Initialize a list to store book recommendations
    recommended_books = []

    # Find books that the target user has not read but the similar users have
    for book_index in range(user_book_matrix.shape[1]):
        book_name = data['name'].iloc[book_index]
        if user_book_matrix.iloc[user_index, book_index] == 0:
            for user in similar_users:
                if user_book_matrix.iloc[user, book_index] > 0:
                    recommended_books.append(book_name)
                    break

        # Stop when reaching the desired number of recommendations
        if len(recommended_books) >= top_n:
            break


    return recommended_books[:top_n]

# Get user-based book recommendations for a user
user_id = 'User1'  # Replace with the desired user
user_recommendations = get_user_based_recommendations(user_id, user_similarity, user_book_matrix, data)

# Print the recommended books for the user
print("Recommended Books for {}: {}".format(user_id, user_recommendations))
