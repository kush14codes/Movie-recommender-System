# Movie Recommender System 🎬

A Netflix-style Movie Recommendation Web App built using Machine Learning, NLP, Streamlit, and TMDB API.

---

# Features

- Content-Based Movie Recommendation System
- Netflix-inspired modern UI
- Movie poster fetching using TMDB API
- Recommendation engine using CountVectorizer and Cosine Similarity
- Streamlit interactive web app

---

# Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- TMDB API

---

# Recommendation Logic

This project uses a **Content-Based Recommendation System**.

## Workflow

1. Movie datasets merged
2. Important features extracted:
   - genres
   - keywords
   - cast
   - crew
   - overview
3. Text preprocessing and stemming
4. CountVectorizer used for vectorization
5. Cosine Similarity used to recommend similar movies

---

# Dataset

Dataset used:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

Dataset source:

https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

# Important Note

The file:

```text
model/similarity.pkl
```

is excluded from this repository because it exceeds GitHub's file size limit.

To regenerate it, run the notebook:

```text
movie recommender.ipynb
```

which recreates all preprocessing, vectorization, and similarity computations.

---

# Run Locally

## Clone Repository

```bash
git clone https://github.com/kush14codes/Movie-recommender-System.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Streamlit App

```bash
streamlit run app.py
```

---

# Screenshots

(Add screenshots here later)

---

# Author

Kushagra Chaubey

GitHub:
https://github.com/kush14codes