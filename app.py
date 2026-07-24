import streamlit as st
from recommender import (
    get_all_movies,
    group_recommend
)

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="WatchTogether AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.stApp{
    background-color:#141414;
    color:white;
}

h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}

section[data-testid="stSidebar"]{
    background-color:#0d0d0d;
}

.stButton>button{
    width:100%;
    background:#E50914;
    color:white;
    border:none;
    border-radius:10px;
    padding:0.8rem;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#B20710;
}

.card{
    background:#1f1f1f;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 0px 15px rgba(0,0,0,0.5);
    text-align:center;
}

.hero{
    background:linear-gradient(90deg,#000000,#1b1b1b);
    border-radius:20px;
    padding:40px;
    margin-bottom:30px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:60px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/4221/4221484.png",
    width=120
)

st.sidebar.title("🎬 WatchTogether AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "👥 Group Recommendation",
        "📈 Analytics",
        "ℹ About"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
Find the perfect movie
for everyone in your group.
"""
)

# ---------------------------------------------------
# HOME
# ---------------------------------------------------

if page=="🏠 Home":

    st.markdown("""
    <div class='hero'>
    <h1>🎬 WatchTogether AI</h1>
    <h3>AI Powered Group Movie Recommendation System</h3>

    <p>
    Find one movie everyone will enjoy using
    Machine Learning and Cosine Similarity.
    </p>

    </div>
    """,unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    with c1:

        st.markdown("""
        <div class='card'>
        <h2>👥</h2>
        <h3>Group Recommendation</h3>
        <p>
        Combine preferences
        of multiple friends.
        </p>
        </div>
        """,unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class='card'>
        <h2>🤖</h2>
        <h3>AI Recommendation</h3>
        <p>
        Content Based
        Movie Recommendation.
        </p>
        </div>
        """,unsafe_allow_html=True)

    with c3:

        st.markdown("""
        <div class='card'>
        <h2>🎯</h2>
        <h3>Cosine Similarity</h3>
        <p>
        Smart similarity based
        recommendation.
        </p>
        </div>
        """,unsafe_allow_html=True)

# ---------------------------------------------------
# GROUP RECOMMENDER
# ---------------------------------------------------
# ---------------------------------------------------
# GROUP RECOMMENDER
# ---------------------------------------------------

elif page == "👥 Group Recommendation":

    st.title("👥 Group Movie Recommendation")

    st.write("Select one favourite movie for each friend.")

    movie_list = get_all_movies()

    col1, col2 = st.columns(2)

    with col1:

        friend1 = st.selectbox("Friend 1", movie_list)

        friend2 = st.selectbox(
            "Friend 2",
            movie_list,
            index=1
        )

    with col2:

        friend3 = st.selectbox(
            "Friend 3",
            movie_list,
            index=2
        )

        friend4 = st.selectbox(
            "Friend 4",
            movie_list,
            index=3
        )

    st.write("")

    if st.button("🎯 Recommend Movies"):

        inputs = [
            friend1,
            friend2,
            friend3,
            friend4
        ]

        results = group_recommend(inputs)

        if len(results) == 0:

            st.error("No recommendations found.")

        else:

            st.success("Recommendations generated!")

            st.subheader("Top Movie Recommendations")

            for i, movie in enumerate(results, start=1):

                st.markdown("---")

                st.markdown(f"## {i}. {movie['title']}")

                st.write(f"👥 Votes : {movie['votes']}")

                st.write(
                    f"⭐ Average Similarity : {movie['average_score']:.3f}"
                )

                st.write(
                    f"🔥 Total Score : {movie['total_score']:.3f}"
                )
# ---------------------------------------------------
# ANALYTICS
# ---------------------------------------------------

elif page=="📈 Analytics":

    st.title("📈 Analytics")

    st.metric("Movies",4800)

    st.metric("Users",4)

    st.metric("Average Similarity","0.81")

# ---------------------------------------------------
# ABOUT
# ---------------------------------------------------

elif page=="ℹ About":

    st.title("About")

    st.write("""

WatchTogether AI

Content Based Movie Recommendation

Built using

- Python

- Pandas

- Scikit-learn

- Streamlit

- Cosine Similarity

""")

# ---------------------------------------------------

