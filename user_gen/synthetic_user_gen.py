import random
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from helper.preprocessing import makeDataset

st.set_page_config(layout="wide", page_title="Persona-Based Book Recommendation")

version = '0.1.3'
path = 'data/'
file_name = path + 'novels_' + version + '.csv'
df = pd.read_csv(file_name)

genres = sorted(list(set(','.join(df['genres'].dropna().to_list()).replace('[', '').replace(']', '').replace("'", '').replace(' ', '').replace('"', '').split(','))))
tags = sorted(list(set(','.join(df['tags'].dropna().to_list()).replace('[', '').replace(']', '').replace("'", '').replace(' ', '').replace('"', '').split(','))))
languages = sorted(df['original_language'].dropna().unique().tolist())

def generate_persona(selected_genres, selected_tags, selected_languages):
    persona = {
        'preferred_genres': selected_genres,
        'preferred_tags': selected_tags,
        'preferred_languages': selected_languages,
    }
    return persona


def get_persona_recommendations(persona_vector, data, top_n=5):
    # Create a TF-IDF vectorizer for the book data
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(data['combined_features'])
    
    # generate persona text
    persona_text = ' '.join(persona_vector['preferred_genres'] + persona_vector['preferred_tags'] + persona_vector['preferred_languages'])
    persona_vector = tfidf_vectorizer.transform([persona_text])
    
    # Calculate the cosine similarity between the persona vector and all books
    cosine_sim = linear_kernel(persona_vector, tfidf_matrix)

    # Get the book indices with the highest similarity to the persona
    book_indices = cosine_sim[0].argsort()[::-1]
    
    # Get the top N recommended books
    recommended_books = data['name'].iloc[book_indices[:top_n]]

    return recommended_books


def get_user_history_recommendations(user_books, data, top_n=5):
    # Create a TF-IDF vectorizer for the book data
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(data['combined_features'])
    
    # Calculate the cosine similarity between user_books and all books
    user_books_vector = tfidf_vectorizer.transform(user_books)
    cosine_sim = linear_kernel(user_books_vector, tfidf_matrix)
    # Create an empty array to store the sum of cosine similarity scores
    sum_sim_scores = [0] * len(data)
    # Calculate the sum of cosine similarity scores for each book the user has read
    for i in range(len(user_books)):
        sum_sim_scores += cosine_sim[i]

    # Combine the book indices with their corresponding sum scores
    book_scores = list(enumerate(sum_sim_scores))

    # Sort the books based on the sum of similarity scores
    book_scores = sorted(book_scores, key=lambda x: x[1], reverse=True)
    
    # make sure that the recommended books are not in the user history
    book_scores = [book for book in book_scores if data['name'].iloc[book[0]] not in user_books]

    # Get the top N recommended books
    book_indices = [i[0] for i in book_scores[:top_n]]
    
    # Return the top N recommended books
    return data['name'].iloc[book_indices]

def generate_user_history(persona, num_of_history):
    num = 100
    recommendations = get_persona_recommendations(persona, makeDataset(file_name), num)
    return recommendations.sample(num_of_history).to_list()


if __name__ == "__main__":
    st.title("Persona-Based Book Recommendation")
    
    if 'persona' not in st.session_state:
        st.session_state.persona = {
            'preferred_genres': [],
            'preferred_tags': [],
            'preferred_languages': [],
        }
        
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Dropdowns for selecting genres, tags, and languages
    selected_genres = st.multiselect("Select Preferred Genres", genres)
    selected_tags = st.multiselect("Select Preferred Tags", tags)
    selected_languages = st.multiselect("Select Preferred Original Languages", languages)
    st.subheader("Generate Persona")
    # Button to generate the persona
    if st.button("Generate Persona"):
        st.session_state.persona['preferred_genres'] = selected_genres
        st.session_state.persona['preferred_tags'] = selected_tags
        st.session_state.persona['preferred_languages'] = selected_languages
        st.write("Generated Persona:")
        st.write(st.session_state.persona)

    # Sidebar for navigating between pages
    page = st.sidebar.radio("Select a Recommendation", ["Persona Based", "History Based"])

    if page == "Persona Based":
        st.subheader("Recommend based on Persona")
        # Button to recommend books for the persona
        if st.button("Recommend"):
            persona = st.session_state.persona
            # check if persona is generated
            if persona.get('preferred_genres') is None or persona.get('preferred_tags') is None or persona.get('preferred_languages') is None:
                st.write("Please generate a persona before recommending books.")
            else:
                recommended_books = get_persona_recommendations(persona, makeDataset(file_name))
                st.write("Recommended Books:")
                for book in recommended_books:
                    book_id = df[df['name'] == book]['id'].values[0]
                    st.write(f"[{book}]({'http://www.novelupdates.com/?p=' + f'{book_id}'})")

    if page == "History Based":
        st.subheader("Recommend based on History")
        persona = st.session_state.persona
        history = st.session_state.history
        if st.button("Generate Synthetic History"):
            # random between 0 and 10
            num_of_history = random.randint(3, 15)
            st.session_state.history = generate_user_history(persona, num_of_history)
            st.write("Generated History:")
            for book in st.session_state.history:
                book_id = df[df['name'] == book]['id'].values[0]
                st.write(f"[{book}]({'http://www.novelupdates.com/?p=' + f'{book_id}'})")
            
        if st.button("Recommend"):
            recommended_books = get_user_history_recommendations(history, makeDataset(file_name))
            if len(history) > 0:
                st.write("History:")
                for book in history:
                    book_id = df[df['name'] == book]['id'].values[0]
                    st.write(f"[{book}]({'http://www.novelupdates.com/?p=' + f'{book_id}'})")
            st.write("Recommended Books:")
            for book in recommended_books:
                book_id = df[df['name'] == book]['id'].values[0]
                st.write(f"[{book}]({'http://www.novelupdates.com/?p=' + f'{book_id}'})")