import joblib
import pandas as pd
from sklearn.neighbors import NearestNeighbors


movies = pd.read_pickle("movies.pkl")

tfidf_matrix = joblib.load("tfidf_matrix.pkl")


model = NearestNeighbors(
    n_neighbors=51,
    metric="cosine",
    algorithm="brute"
)

model.fit(tfidf_matrix)


def recommend_movies(title, n=10):

    movie_index = movies[
        movies["title"].str.lower() == title.lower()
    ].index

    if len(movie_index) == 0:
        return None

    movie_index = movie_index[0]

    # Get 50 candidates
    distances, indices = model.kneighbors(
        tfidf_matrix[movie_index],
        n_neighbors=51
    )

    recommendations = []

    for distance, index in zip(
        distances[0][1:],
        indices[0][1:]
    ):

        similarity = 1 - distance

        rating_norm = movies.iloc[index]["rating"] / 5

        final_score = (
            0.75 * similarity +
            0.25 * rating_norm
        )

        recommendations.append({
            "Movie": movies.iloc[index]["title"],
            "Similarity": round(similarity, 3),
            "Rating": movies.iloc[index]["rating"],
            "Final Score": round(final_score, 3)
        })

    recommendations = pd.DataFrame(recommendations)

    recommendations = recommendations.sort_values(
        by="Final Score",
        ascending=False
    )

    return recommendations.head(n)