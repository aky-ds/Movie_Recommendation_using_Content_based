import streamlit as st
import pickle
import numpy as np
# Loading the model

with open('Similarity.pkl','rb') as x:
    similarity=pickle.load(x)
    x.close()

# Loading the pivot

with open('pt.pkl','rb') as x:
    pt=pickle.load(x)
    x.close()

# Creating a title

st.title('Movie Recommendation using Content ')


# Creating an input

movie_name=st.text_input('Enter the movie name')


if st.button('Recommend'):
    index = np.where(pt.index == movie_name)[0][0]

    # Find the most similar movies to the given movies
    similar_movies = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)[1:6]
    st.write('The Recommended movies are:')
    # Print the recommended movies
    for movie_index, _ in similar_movies:  # unpack the tuple (index, similarity)
        st.write(f'*{pt.index[movie_index]}')