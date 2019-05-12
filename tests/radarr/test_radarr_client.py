import pytest
import requests_mock

from nzbclient import RadarrClient

MOCK_URL = "http://localhost:9999"
MOCK_API_KEY = "TEST_API_KEY"


@pytest.fixture()
def client():
    yield RadarrClient(MOCK_URL, MOCK_API_KEY)


def test_movie_get(client, movie_json):
    with requests_mock.Mocker() as m:
        m.get(f"{MOCK_URL}/api/movie/1?apikey={MOCK_API_KEY}", json=movie_json)
        movie = client.get_movie(1)

        # TODO: Test some fields, add more later
        assert movie.title == "Assassin's Creed"
        assert movie.title_slug == "assassins-creed-121856"
        assert movie.quality_profile_id == 6
        assert movie.tmdb_id == 121856


def test_movie_add(client, movie_obj, movie_json):
    with requests_mock.Mocker() as m:
        m.post(f"{MOCK_URL}/api/movie?apikey={MOCK_API_KEY}", json=movie_json)
        movie = client.add_movie(movie_obj)

        # TODO: Test some fields, add more later
        assert movie.title == "Assassin's Creed"
        assert movie.title_slug == "assassins-creed-121856"
        assert movie.quality_profile_id == 6
        assert movie.tmdb_id == 121856
