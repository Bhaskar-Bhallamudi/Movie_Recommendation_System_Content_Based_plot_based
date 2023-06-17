import pickle
import streamlit as st
import requests

def movie_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def movie_recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(movie_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

st.title(':violet[Movie Recommender System]')
movies= pickle.load(open(r"C:\Users\bhask\Desktop\DATA SCIENCE AND ANALYTICS\Internship_Inno\FINAL_INTERNSHIP_PROJECT\Movie_Recommendation_Deployment\movie_list_new.pkl", 'rb'))
similarity = pickle.load(open(r"C:\Users\bhask\Desktop\DATA SCIENCE AND ANALYTICS\Internship_Inno\FINAL_INTERNSHIP_PROJECT\Movie_Recommendation_Deployment\cosine_simil_new.pkl", 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox( ":blue[Look and select a movie in the drop-down or enter a movie name]",movie_list)

if st.button('Show Recommendation'):
    st.snow()
    st.markdown("https://www.linkedin.com/in/bhaskar-bhallamudi-6a7a511ba/")
    recommended_movie_names,recommended_movie_posters = movie_recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.subheader(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.subheader(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.subheader(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.subheader(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.subheader(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])