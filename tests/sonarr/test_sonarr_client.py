import pytest
import requests_mock

from nzbclient import SonarrClient

MOCK_URL = "http://localhost:9999"
MOCK_API_KEY = "TEST_API_KEY"


@pytest.fixture()
def client():
    yield SonarrClient(MOCK_URL, MOCK_API_KEY)


def test_series_add(client, series_obj, series_json):
    with requests_mock.Mocker() as m:
        m.post(f"{MOCK_URL}/api/series?apikey={MOCK_API_KEY}", json=series_json)
        series = client.add_series(series_obj)

        # TODO: Test some fields, add more later
        assert series.title == series_obj.title
        assert series.title_slug == series_obj.title_slug
        assert series.quality_profile_id == series_obj.quality_profile_id
        assert series.tvdb_id == series_obj.tvdb_id


def test_episode_update(client, episode_obj, episode_json):
    with requests_mock.Mocker() as m:
        m.put(f"{MOCK_URL}/api/episode?apikey={MOCK_API_KEY}", json=episode_json)
        episode = client.update_episode(episode_obj)

        # TODO: Test some fields, add more later
        assert episode.title == episode_obj.title
