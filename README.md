# 🎬 Movie Recommendation System

A content-based movie recommendation system built using **Python, Pandas, Scikit-learn, and Streamlit**.

The system recommends movies similar to a movie selected by the user by analyzing movie metadata such as genres, themes, directors, actors, and descriptions.

---

## 🚀 Live Demo

🔗 **Streamlit App:**  
https://movie-recommendation-system-h68tjn9jwbvboue2ixrmhe.streamlit.app/

---

## 📌 Project Overview

This project implements a **content-based filtering recommendation system**.

Instead of relying on ratings from other users, the system analyzes the characteristics of movies and finds movies with similar content.

For example, if a user searches for:

> `Interstellar`

the system identifies movies with similar genres, themes, directors, actors, and descriptions and recommends the most similar titles.

---

## 🧠 How It Works

The recommendation pipeline consists of the following steps:

```text
Movie Dataset
      ↓
Data Preprocessing
      ↓
Combine Movie Metadata
      ↓
TF-IDF Vectorization
      ↓
Nearest Neighbors
      ↓
Cosine Similarity
      ↓
Rating-Based Re-ranking
      ↓
Top Movie Recommendations

<img width="1906" height="903" alt="image" src="https://github.com/user-attachments/assets/a232c63c-a527-4329-a6f1-7a612883fa5b" />

