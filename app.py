import streamlit as st
from recommender import recommend_movies


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🎬 Movie Recommendation System")

st.write(
    "Find movies similar to your favorite movie "
    "using content-based filtering."
)


# --------------------------------------------------
# Movie input
# --------------------------------------------------

movie_name = st.text_input(
    "Enter a movie name",
    placeholder="e.g. Interstellar"
)


# --------------------------------------------------
# Number of recommendations
# --------------------------------------------------

number_of_movies = st.slider(
    "Number of recommendations",
    min_value=5,
    max_value=20,
    value=10
)


# --------------------------------------------------
# Recommendation button
# --------------------------------------------------

if st.button("🎯 Recommend Movies"):

    if movie_name.strip() == "":
        st.warning("Please enter a movie name.")

    else:

        with st.spinner("Finding similar movies..."):

            results = recommend_movies(
                movie_name,
                n=number_of_movies
            )

        if results is None:

            st.error(
                f"❌ '{movie_name}' was not found in the dataset."
            )

        else:

            st.success(
                f"Movies similar to **{movie_name.title()}**"
            )

            st.dataframe(
                results,
                use_container_width=True,
                hide_index=True
            )