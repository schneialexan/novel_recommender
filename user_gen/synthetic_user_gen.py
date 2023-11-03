from enum import unique
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from helper.preprocessing import makeDataset

version = '0.1.3'
path = ''
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


if __name__ == "__main__":
    st.title("Persona-Based Book Recommendation")
    
    if 'persona' not in st.session_state:
        st.session_state.persona = {
            'preferred_genres': [],
            'preferred_tags': [],
            'preferred_languages': [],
        }

    # Dropdowns for selecting genres, tags, and languages
    selected_genres = st.multiselect("Select Preferred Genres", genres)
    selected_tags = st.multiselect("Select Preferred Tags", tags)
    selected_languages = st.multiselect("Select Preferred Original Languages", languages)

    # Button to generate the persona
    if st.button("Generate Persona"):
        st.session_state.persona['preferred_genres'] = selected_genres
        st.session_state.persona['preferred_tags'] = selected_tags
        st.session_state.persona['preferred_languages'] = selected_languages
        st.write("Generated Persona:")
        st.write(st.session_state.persona)

    # Button to recommend books for the persona
    if st.button("Recommend Books"):
        persona = st.session_state.persona
        # check if persona is generated
        if persona.get('preferred_genres') is None or persona.get('preferred_tags') is None or persona.get('preferred_languages') is None:
            st.write("Please generate a persona before recommending books.")
        else:
            print(f'Generating recommendations...')
            
            recommended_books = get_persona_recommendations(persona, makeDataset())
            st.write("Recommended Books:")
            for book in recommended_books:
                book_id = df[df['name'] == book]['id'].values[0]
                print(f'book_id: {book_id}')
                st.write(f"[{book}]({'http://www.novelupdates.com/?p=' + f'{book_id}'})")
