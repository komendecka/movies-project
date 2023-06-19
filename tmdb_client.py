import random

import requests


# def get_movies(how_many):
#     data = get_popular_movies()
#     # rnd_data = []
#     # for _ in how_many:
#     #     rnd_data.append(data["results"][random.randint(0, 500)])
#     # return rnd_data
#     # return data["results"][:how_many]
#     return [data["results"][random.randint(0, 500)] for _ in how_many]

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNWY2MzJjZmQwOTMyN2VjYWU4ODczYWFhZjU3MWM0YyIsInN1YiI6IjY0OGFkNjViYzNjODkxMDBhZTRmNTc5YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.apHBqfH6oqvC3HwaGfjgJYzuZS-vsCx_5V5RjF_9yeo"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


