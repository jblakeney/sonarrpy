from sonarrpy import SonarrClient


if __name__ == "__main__":
    client = SonarrClient("http://server-pc:8989", "49095f567f67413cb5956f8032950f7e")
    print(client.get_episode(episode_id=1))

    print(client.get_episode(series_id=1))
