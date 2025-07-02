import streamlit as st
import pandas as pd
import pickle
import requests


movie_dict=pickle.load(open("movie_dict.pkl","rb"))
movies=pd.DataFrame(movie_dict)
simimlarity=pickle.load(open("similarity.pkl","rb"))


def fetch_poster(movie_id):
   response=  requests.get("https://api.themoviedb.org/3/movie/{}?api_key=2233b7fd14e36de994b4782614c65951&language=en-US".format(movie_id))
   data=response.json()
   return " https://image.tmdb.org/t/p/w500/" + data['poster_path']
    




def Recommended(movie):
    if movie not in movies["title"].values:
        return "This movie is not available in our database"
    movie_index=movies[movies["title"]==movie].index[0]
    distances=simimlarity[movie_index]  
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
        
     
        recommended_movies.append(movies.iloc[i[0]].title)
           # Fetching poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
      
    return recommended_movies, recommended_movies_posters






  

st.title("Movie Recommendation System")

selected_movie_name=st.selectbox(
    "how would you like to be called?",
    movies["title"].values
    )

if st.button("recommend"):
    names,poster= Recommended(selected_movie_name)
    col1, col2, col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])

   