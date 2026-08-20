# 🎬 Movie Recommender System

A content-based movie recommender system built with **pandas**, **scikit-learn**
(`CountVectorizer` + `cosine_similarity`), and a **Streamlit** web UI — same stack
and layout as the classic [Movie-Recommender-System-Using-Machine-Learning](https://github.com/entbappy/Movie-Recommender-System-Using-Machine-Learning)
project, rebuilt from scratch.

## How it works

Each movie's overview, genres, keywords, cast, and crew are combined into a single
`tags` string, stemmed with NLTK's `PorterStemmer`, vectorized with
`CountVectorizer(max_features=5000, stop_words="english")`, and compared pairwise
with `cosine_similarity`. Given a movie, the app returns the 5 most similar titles.

## Project structure

```
movie-recommender-system/
├── artifacts/                     # generated .pkl model artifacts (created on first run)
├── data/
│   └── movies.csv                 # sample dataset (30 movies) — swap for the full TMDB 5000 set
├── notebook/
│   └── Movie_Recommender_System_Data_Analysis.ipynb
├── demo/                          # app screenshots
├── src/mrs/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   └── training_pipeline.py
│   ├── logger.py
│   ├── exception.py
│   └── utils.py
├── app.py                         # Streamlit app
├── requirements.txt
├── setup.py
├── setup.sh                       # Streamlit config for cloud deployment
├── Procfile                       # for Heroku-style platforms
└── LICENSE
```

## Dataset

This repo ships with a small 30-movie sample (`data/movies.csv`) so the pipeline
runs end-to-end out of the box. For a real app, swap it for the
[TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata) from
Kaggle — keep the same column names (`movie_id`, `title`, `overview`, `genres`,
`keywords`, `cast`, `crew`) or adjust `data_transformation.py` accordingly.

## How to run

### 1. Clone and create an environment

```bash
git clone <your-repo-url>
cd movie-recommender-system
conda create -n mrs python=3.10 -y
conda activate mrs
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Generate the model artifacts

Either run the training pipeline:

```bash
python -m src.mrs.pipeline.training_pipeline
```

or run the notebook `notebook/Movie_Recommender_System_Data_Analysis.ipynb` cell by
cell — both produce `artifacts/movie_list.pkl` and `artifacts/similarity.pkl`.

### 4. Launch the app

```bash
streamlit run app.py
```

### Optional: real posters

Set a free [TMDB API key](https://www.themoviedb.org/settings/api) as an
environment variable to show real poster art instead of placeholders:

```bash
export TMDB_API_KEY=your_key_here   # Windows: set TMDB_API_KEY=your_key_here
```

## Deploying

**Streamlit Community Cloud** (recommended, free): push this repo to GitHub, go to
[share.streamlit.io](https://share.streamlit.io), point it at `app.py`, and add
`TMDB_API_KEY` under app settings → secrets. Make sure `artifacts/*.pkl` exist —
either commit them or add a build step that runs the training pipeline first.

**Heroku-style platforms**: the included `Procfile` and `setup.sh` run
`streamlit run app.py` behind the platform's assigned `$PORT`.

## License

MIT — see [LICENSE](LICENSE).
