import requests

# ----------------------------------------
# TMDB API KEY
# ----------------------------------------

TMDB_API_KEY = "YOUR_API_KEY"

BASE_URL = "https://api.themoviedb.org/3"

POSTER_URL = "https://image.tmdb.org/t/p/w500"


# ----------------------------------------
# Search Movie by Name
# ----------------------------------------

def search_movie(movie_name):

    url = f"{BASE_URL}/search/movie"

    params = {

        "api_key": TMDB_API_KEY,

        "query": movie_name

    }

    response = requests.get(url, params=params)

    data = response.json()

    if len(data["results"]) == 0:

        return None

    return data["results"][0]


# ----------------------------------------
# Fetch Poster
# ----------------------------------------

def fetch_poster(movie_name):

    movie = search_movie(movie_name)

    if movie is None:

        return "https://via.placeholder.com/500x750?text=No+Poster"

    if movie["poster_path"] is None:

        return "https://via.placeholder.com/500x750?text=No+Poster"

    return POSTER_URL + movie["poster_path"]


# ----------------------------------------
# Rating
# ----------------------------------------

def fetch_rating(movie_name):

    movie = search_movie(movie_name)

    if movie is None:

        return "N/A"

    return movie["vote_average"]


# ----------------------------------------
# Release Year
# ----------------------------------------

def fetch_year(movie_name):

    movie = search_movie(movie_name)

    if movie is None:

        return "N/A"

    return movie["release_date"][:4]


# ----------------------------------------
# Overview
# ----------------------------------------

def fetch_overview(movie_name):

    movie = search_movie(movie_name)

    if movie is None:

        return ""

    return movie["overview"]


# ----------------------------------------
# TMDB Movie ID
# ----------------------------------------

def fetch_movie_id(movie_name):

    movie = search_movie(movie_name)

    if movie is None:

        return None

    return movie["id"]


# ----------------------------------------
# Full Movie Details
# ----------------------------------------

def fetch_details(movie_name):

    movie_id = fetch_movie_id(movie_name)

    if movie_id is None:

        return None

    url = f"{BASE_URL}/movie/{movie_id}"

    params = {

        "api_key": TMDB_API_KEY

    }

    response = requests.get(

        url,

        params=params

    )

    return response.json()


# ----------------------------------------
# Runtime
# ----------------------------------------

def fetch_runtime(movie_name):

    details = fetch_details(movie_name)

    if details is None:

        return "N/A"

    return details["runtime"]


# ----------------------------------------
# Genres
# ----------------------------------------

def fetch_genres(movie_name):

    details = fetch_details(movie_name)

    if details is None:

        return []

    genres = []

    for genre in details["genres"]:

        genres.append(

            genre["name"]

        )

    return genres


# ----------------------------------------
# Language
# ----------------------------------------

def fetch_language(movie_name):

    details = fetch_details(movie_name)

    if details is None:

        return "N/A"

    return details["original_language"]


# ----------------------------------------
# Trailer
# ----------------------------------------

def fetch_trailer(movie_name):

    movie_id = fetch_movie_id(movie_name)

    if movie_id is None:

        return None

    url = f"{BASE_URL}/movie/{movie_id}/videos"

    params = {

        "api_key": TMDB_API_KEY

    }

    response = requests.get(

        url,

        params=params

    )

    data = response.json()

    for video in data["results"]:

        if video["site"] == "YouTube":

            return "https://www.youtube.com/watch?v=" + video["key"]

    return None


# ----------------------------------------
# Complete Movie Information
# ----------------------------------------

def movie_card(movie_name):

    return {

        "title": movie_name,

        "poster": fetch_poster(movie_name),

        "rating": fetch_rating(movie_name),

        "year": fetch_year(movie_name),

        "overview": fetch_overview(movie_name),

        "runtime": fetch_runtime(movie_name),

        "genres": fetch_genres(movie_name),

        "language": fetch_language(movie_name),

        "trailer": fetch_trailer(movie_name)

    }


# ----------------------------------------
# Testing
# ----------------------------------------

if __name__ == "__main__":

    movie = movie_card("Avatar")

    print(movie)