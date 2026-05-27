import pickle
import streamlit as st
import requests

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Netflix Style Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.stApp {
    background-color: #0b0f1a;
    color: white;
}

.hero {
    text-align: center;
    padding-top: 20px;
    padding-bottom: 20px;
}

.hero h1 {
    font-size: 60px;
    color: #E50914;
    font-weight: 800;
    margin-bottom: 10px;
}

.hero p {
    font-size: 20px;
    color: #d1d1d1;
}

.movie-card {
    background-color: #141414;
    padding: 10px;
    border-radius: 14px;
    transition: 0.3s;
    text-align: center;
}

.movie-card:hover {
    transform: scale(1.05);
}

.stButton > button {
    width: 100%;
    background: linear-gradient(to right, #E50914, #ff4b2b);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 14px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
    background: linear-gradient(to right, #ff4b2b, #E50914);
}

.stSelectbox label {
    color: white !important;
    font-size: 18px;
    font-weight: bold;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------- FETCH POSTER ---------------- #

API_KEY = "0ffd88b4d973a68338ffd645867433f2"


def fetch_poster(movie_id):

    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=0ffd88b4d973a68338ffd645867433f2&language=en-US"

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return "https://via.placeholder.com/500x750?text=API+Error"

        data = response.json()

        poster_path = data.get('poster_path')

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"

        return "https://via.placeholder.com/500x750?text=No+Poster"

    except:
        return "https://via.placeholder.com/500x750?text=Connection+Error"


# ---------------- RECOMMEND FUNCTION ---------------- #

def recommend(movie):

    index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:

        movie_id = movies.iloc[i[0]].movie_id

        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


# ---------------- LOAD DATA ---------------- #

movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))


# ---------------- HERO SECTION ---------------- #

st.markdown("""
<div class='hero'>
    <h1>🎬 MOVIE RECOMMENDER</h1>
    <p>Discover movies you'll love instantly</p>
</div>
""", unsafe_allow_html=True)


# ---------------- MOVIE SELECT ---------------- #

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Search your favourite movie",
    movie_list
)


# ---------------- RECOMMEND BUTTON ---------------- #

if st.button('🔥 Recommend Movies'):

    with st.spinner('Finding awesome movies for you...'):

        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

        st.markdown("## 🍿 Recommended For You")

        cols = st.columns(5)

        for idx, col in enumerate(cols):

            with col:

                st.markdown("<div class='movie-card'>", unsafe_allow_html=True)

                st.image(recommended_movie_posters[idx])

                st.markdown(
                    f"""
                    <h4 style='text-align:center; color:white;'>
                    {recommended_movie_names[idx]}
                    </h4>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown("</div>", unsafe_allow_html=True)


# ---------------- FOOTER ---------------- #

st.markdown("---")
st.markdown(
    "<center style='color:gray;'>Built with ❤️ using Streamlit & Machine Learning</center>",
    unsafe_allow_html=True
)