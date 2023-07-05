import tmdb_client
import app
import pytest
from unittest.mock import Mock


def test_get_poster_url_uses_default_size():
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    assert expected_default_size in poster_url


def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list is not None


def test_get_movies_list(monkeypatch):
    mock_movies_list = ['Movie 1', 'Movie 2']
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list


def test_get_single_movie_not_none():
    response = tmdb_client.get_single_movie(650747)
    assert response is not None


def test_get_single_movie_cast_not_none():
    response = tmdb_client.get_single_movie_cast(650747)
    assert response is not None


def test_get_movie_images_not_none():
    response = tmdb_client.get_movie_images(650747)
    assert response is not None


def test_call_tmdb_api_for_content(monkeypatch):
    mock_api = 'mock'
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_api
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    endpoint = "movie/popular"  # Przykładowy endpoint
    api = tmdb_client.call_tmdb_api(endpoint)
    assert api == mock_api

