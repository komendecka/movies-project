import random

import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNWY2MzJjZmQwOTMyN2VjYWU4ODczYWFhZjU3MWM0YyIsInN1YiI6IjY0OGFkNjViYzNjODkxMDBhZTRmNTc5YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.apHBqfH6oqvC3HwaGfjgJYzuZS-vsCx_5V5RjF_9yeo"

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return [data["results"][random.randint(0, 19)] for _ in range(how_many)]


# def get_movies(how_many, list_type):
#     data = get_movies_list(list_type)
#     return data["results"][:how_many]


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()



def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]



