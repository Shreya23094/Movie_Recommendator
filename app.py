import streamlit as st
import pickle
import pandas as pd

movie_dict=pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    mindex=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movies=[]
    for i in mindex:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

st.title('Movie Recommend System')

selected_movie=st.selectbox(
    'How would you like to be connected',
    (movies['title'].values)

)

if st.button('Recommend'):
    recommended=recommend(selected_movie)
    for i in recommended:
        st.write(i)