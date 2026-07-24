#=========================================================== 🎬
WatchTogether AI - Group Movie Recommendation System
===========================================================

Author: Sanyukta Saha

Project Type: Machine Learning | Recommendation System | Streamlit

  ------------------
  PROJECT OVERVIEW
  ------------------

WatchTogether AI is a Content-Based Group Movie Recommendation System
built using Machine Learning.

Instead of recommending movies for a single user, the system combines
the preferences of multiple users and recommends movies that the entire
group is likely to enjoy.

The recommendation engine uses cosine similarity on movie metadata
including: • Overview • Genres • Keywords • Cast • Director

The application is deployed with Streamlit and provides an interactive
user interface for selecting favourite movies from multiple friends.

  ----------
  FEATURES
  ----------

✔ Content-Based Recommendation ✔ Group Recommendation ✔ Cosine
Similarity Ranking ✔ Multiple User Preference Aggregation ✔ Fast
Recommendation Engine ✔ Streamlit User Interface ✔ Dark Netflix-inspired
Theme

  ---------
  DATASET
  ---------

TMDB 5000 Movie Dataset

Columns used: • Movie Title • Overview • Genres • Keywords • Cast • Crew
(Director)

  ---------------------------
  MACHINE LEARNING PIPELINE
  ---------------------------

1.  Data Cleaning
2.  JSON Parsing
3.  Feature Engineering
4.  Metadata Combination
5.  Text Vectorization
6.  CountVectorizer
7.  Cosine Similarity Matrix
8.  Group Score Aggregation

  ------------
  TECH STACK
  ------------

Python Pandas NumPy Scikit-learn Pickle Streamlit

  -------------------
  PROJECT STRUCTURE
  -------------------

WatchTogether-AI/

├── app.py ├── recommender.py ├── helper.py ├── style.css ├── movies.pkl
├── similarity.pkl ├── requirements.txt └── README.md

  ------------
  HOW TO RUN
  ------------

1.  Install dependencies

pip install -r requirements.txt

2.  Run the application

streamlit run app.py

  ---------------------
  FUTURE IMPROVEMENTS
  ---------------------

• Hybrid Recommendation System • Collaborative Filtering • Personalized
User Profiles • TMDB Poster Integration • LLM-powered Natural Language
Search • Mood-Based Recommendations • User Authentication

  ---------
  LICENSE
  ---------

Educational and Portfolio Project

===========================================================
