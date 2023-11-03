from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity, laplacian_kernel, polynomial_kernel, rbf_kernel, sigmoid_kernel
from helper.preprocessing import makeDataset
import numpy as np

def my_cosine_similarity(matrix1, matrix2):
    similarity_matrix = matrix1 @ matrix2.T 
    norm_matrix1 = np.linalg.norm(matrix1, axis=1)  # Compute the norm of rows in matrix1
    norm_matrix2 = np.linalg.norm(matrix2, axis=1)  # Compute the norm of rows in matrix2

    # Handle cases where one of the norms is zero to avoid division by zerotask
    norm_matrix1[norm_matrix1 == 0] = 1
    norm_matrix2[norm_matrix2 == 0] = 1

    # Calculate cosine similarity matrix
    similarity_matrix = similarity_matrix / (norm_matrix1[:, np.newaxis] * norm_matrix2)

    return similarity_matrix

# Load the data into a DataFrame
data = makeDataset()
# Create TF-IDF vectorizer to convert text data into numerical vectors
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(data['combined_features'])

# Compute the similarity between books
linear_ker = linear_kernel(tfidf_matrix, tfidf_matrix)
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
laplacian_ker = laplacian_kernel(tfidf_matrix, tfidf_matrix)
polynomial_ker = polynomial_kernel(tfidf_matrix, tfidf_matrix)
rbf_ker = rbf_kernel(tfidf_matrix, tfidf_matrix)
sigmoid_ker = sigmoid_kernel(tfidf_matrix, tfidf_matrix)
my_cosine_sim = my_cosine_similarity(tfidf_matrix, tfidf_matrix)


# Function to recommend novels based on similarity
def get_recommendations(book_name, cosine_sim=cosine_sim):
    book_index = data[data['name'] == book_name].index[0]
    similar_books = list(enumerate(cosine_sim[book_index]))
    similar_books = sorted(similar_books, key=lambda x: x[1], reverse=True)
    similar_books = similar_books[1:11]  # Get the top 10 similar books
    book_indices = [x[0] for x in similar_books]
    return data['name'].iloc[book_indices]

book_name = "Reborn into Naruto World with Tenseigan"
recommendations_cos = get_recommendations(book_name, cosine_sim)
recommendations_linear = get_recommendations(book_name, linear_ker)
recommendations_laplacian = get_recommendations(book_name, laplacian_ker)
recommendations_polynomial = get_recommendations(book_name, polynomial_ker)
recommendations_rbf = get_recommendations(book_name, rbf_ker)
recommendations_sigmoid = get_recommendations(book_name, sigmoid_ker)
recommendations_my_cosine = get_recommendations(book_name, my_cosine_sim)


print(f'Recommendations for Book: {book_name}')
for i in range(3):
    print(f'Cosine: {recommendations_cos.iloc[i]}')
    print(f'My Cosine: {recommendations_my_cosine.iloc[i]}')
    print(f'Linear: {recommendations_linear.iloc[i]}')
    print(f'Laplacian: {recommendations_laplacian.iloc[i]}')
    print(f'Polynomial: {recommendations_polynomial.iloc[i]}')
    print(f'RBF: {recommendations_rbf.iloc[i]}')
    print(f'Sigmoid: {recommendations_sigmoid.iloc[i]}')
    print('\n')
