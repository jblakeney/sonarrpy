from nzbclient import SonarrClient


def test_client():
    SonarrClient("http://localhost:9999", "TEST_API_KEY")
