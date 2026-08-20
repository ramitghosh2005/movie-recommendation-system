import os

import requests
import streamlit as st

from src.mrs.utils import load_object

MOVIE_LIST_PATH = os.path.join("artifacts", "movie_list.pkl")
SIMILARITY_PATH = os.path.join("artifacts", "similarity.pkl")

# Optional: set a TMDB API key as an environment variable to fetch real posters.
# Get a free key at https://www.themoviedb.org/settings/api
TMDB_API_KEY = os.environ.get("TMDB_API_KEY", "")


def fetch_poster(movie_title: str) -> str:
    """Fetch a poster from TMDB by movie title. Falls back to a placeholder
    image if no API key is configured or the movie can't be found."""
    if not TMDB_API_KEY:
        return "https://via.placeholder.com/300x450.png?text=" + movie_title.replace(" ", "+")

    try:
        response = requests.get(
            "https://api.themoviedb.org/3/search/movie",
            params={"api_key": TMDB_API_KEY, "query": movie_title},
            timeout=5,
        )
        data = response.json()
        results = data.get("results", [])
        if results and results[0].get("poster_path"):
            return "https://image.tmdb.org/t/p/w500/" + results[0]["poster_path"]
    except requests.exceptions.RequestException:
        pass

    return "https://via.placeholder.com/300x450.png?text=" + movie_title.replace(" ", "+")


def recommend(movie_title: str, movies, similarity, top_n: int = 5):
    index = movies[movies["title"] == movie_title].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1]
    )

    recommended_titles = []
    recommended_posters = []
    for i, _score in distances[1 : top_n + 1]:
        title = movies.iloc[i]["title"]
        recommended_titles.append(title)
        recommended_posters.append(fetch_poster(title))

    return recommended_titles, recommended_posters


st.set_page_config(page_title="Movie Recommender System", page_icon="🎬")
st.title("🎬 Movie Recommender System")
st.write(
    "Content-based movie recommendations powered by CountVectorizer + cosine similarity."
)

if not (os.path.exists(MOVIE_LIST_PATH) and os.path.exists(SIMILARITY_PATH)):
    st.error(
        "Model artifacts not found. Run the training pipeline first:\n\n"
        "`python -m src.mrs.pipeline.training_pipeline`"
    )
    st.stop()

movies = load_object(MOVIE_LIST_PATH)
similarity = load_object(SIMILARITY_PATH)

movie_list = movies["title"].values
selected_movie = st.selectbox("Type or select a movie you like:", movie_list)

if st.button("Show Recommendations"):
    names, posters = recommend(selected_movie, movies, similarity)

    cols = st.columns(len(names))
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            st.image(poster)
