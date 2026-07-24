
from collections import defaultdict

import pickle

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))



def get_all_movies():
    return sorted(movies["title"].tolist())


def recommend(movie_name, top_n=10):

    if movie_name not in movies["title"].values:
        return []

    index = movies[movies["title"] == movie_name].index[0]

    distances = list(enumerate(similarity[index]))

    distances = sorted(
        distances,
        key=lambda x: x[1],
        reverse=True
    )[1:top_n+1]

    recommendations = []

    for idx, score in distances:
        recommendations.append({
            "title": movies.iloc[idx]["title"],
            "score": float(score)
        })

    return recommendations


def recommend_with_scores(movie_name, top_n=20):

    if movie_name not in movies["title"].values:
        return []

    index = movies[movies["title"] == movie_name].index[0]

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:top_n+1]

    return [
        (movies.iloc[idx]["title"], float(score))
        for idx, score in movie_list
    ]


def group_recommend(movie_list, top_n=10):

    scores = defaultdict(float)
    votes = defaultdict(int)

    for movie in movie_list:

        recs = recommend_with_scores(movie)

        for title, score in recs:

            if title not in movie_list:
                scores[title] += score
                votes[title] += 1

    results = []

    for movie in scores:

        results.append({
            "title": movie,
            "votes": votes[movie],
            "average_score": scores[movie] / votes[movie],
            "total_score": scores[movie]
        })

    results = sorted(
        results,
        key=lambda x: (x["votes"], x["average_score"]),
        reverse=True
    )

    return results[:top_n]


def search_movie(query):

    return movies[
        movies["title"]
        .str.lower()
        .str.contains(query.lower(), na=False)
    ]["title"].tolist()