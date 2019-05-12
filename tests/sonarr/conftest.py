import pytest
import json
from datetime import datetime

from nzbclient.sonarr.series import (
    Series,
    AlternateTitle,
    Ratings,
    Image,
    Season,
    Statistics,
)


@pytest.fixture()
def series_obj():
    series = Series(
        title="Marvel's Daredevil",
        alternate_titles=[AlternateTitle(title="Daredevil", season_number=-1)],
        sort_title="marvels daredevil",
        season_count=2,
        total_episode_count=26,
        episode_count=26,
        episode_file_count=26,
        size_on_disk=79282273693,
        status="continuing",
        overview="Matt Murdock was blinded in a tragic accident as a boy, but imbued with extraordinary senses. Murdock sets up practice in his old neighborhood of Hell's Kitchen, New York, where he now fights against injustice as a respected lawyer by day and as the masked vigilante Daredevil by night.",
        previous_airing=datetime(2016, 3, 18, 4, 1),
        network="Netflix",
        air_time="00:01",
        images=[
            Image(
                cover_type="fanart",
                url="/sonarr/MediaCover/7/fanart.jpg?lastWrite=636072351904299472",
            ),
            Image(
                cover_type="banner",
                url="/sonarr/MediaCover/7/banner.jpg?lastWrite=636071666185812942",
            ),
            Image(
                cover_type="poster",
                url="/sonarr/MediaCover/7/poster.jpg?lastWrite=636071666195067584",
            ),
        ],
        seasons=[
            Season(
                season_number=1,
                monitored=False,
                statistics=Statistics(
                    previous_airing=datetime(2015, 4, 10, 4, 1),
                    episode_file_count=13,
                    episode_count=13,
                    total_episode_count=13,
                    size_on_disk=22738179333,
                    percent_of_episodes=100,
                ),
            ),
            Season(
                season_number=2,
                monitored=False,
                statistics=Statistics(
                    previous_airing=datetime(2016, 3, 18, 4, 1),
                    episode_file_count=13,
                    episode_count=13,
                    total_episode_count=13,
                    size_on_disk=56544094360,
                    percent_of_episodes=100,
                ),
            ),
        ],
        year=2015,
        path="F:/TV_Shows/Marvels Daredevil",
        profile_id=6,
        season_folder=True,
        monitored=True,
        use_scene_numbering=False,
        runtime=55,
        tvdb_id=281662,
        tv_rage_id=38796,
        tv_maze_id=1369,
        first_aired=datetime(2015, 4, 10, 4),
        last_info_sync=datetime(2016, 9, 9, 9, 2, 49, 440257),
        series_type="standard",
        clean_title="marvelsdaredevil",
        imdb_id="tt3322312",
        title_slug="marvels-daredevil",
        certification="TV-MA",
        genres=["Action", "Crime", "Drama"],
        tags=[],
        added=datetime(2015, 5, 15, 0, 20, 32, 789274),
        ratings=Ratings(votes=461, value=8.9),
        quality_profile_id=6,
        id=7,
    )

    yield series


@pytest.fixture()
def series_json():
    yield json.loads(
        """{
        "title": "Marvel's Daredevil",
        "alternateTitles": [{
          "title": "Daredevil",
          "seasonNumber": -1
        }],
        "sortTitle": "marvels daredevil",
        "seasonCount": 2,
        "totalEpisodeCount": 26,
        "episodeCount": 26,
        "episodeFileCount": 26,
        "sizeOnDisk": 79282273693,
        "status": "continuing",
        "overview": "Matt Murdock was blinded in a tragic accident as a boy, but imbued with extraordinary senses. Murdock sets up practice in his old neighborhood of Hell's Kitchen, New York, where he now fights against injustice as a respected lawyer by day and as the masked vigilante Daredevil by night.",
        "previousAiring": "2016-03-18T04:01:00Z",
        "network": "Netflix",
        "airTime": "00:01",
        "images": [{
          "coverType": "fanart",
          "url": "/sonarr/MediaCover/7/fanart.jpg?lastWrite=636072351904299472"
        },
        {
          "coverType": "banner",
          "url": "/sonarr/MediaCover/7/banner.jpg?lastWrite=636071666185812942"
        },
        {
          "coverType": "poster",
          "url": "/sonarr/MediaCover/7/poster.jpg?lastWrite=636071666195067584"
        }],
        "seasons": [{
          "seasonNumber": 1,
          "monitored": false,
          "statistics": {
            "previousAiring": "2015-04-10T04:01:00Z",
            "episodeFileCount": 13,
            "episodeCount": 13,
            "totalEpisodeCount": 13,
            "sizeOnDisk": 22738179333,
            "percentOfEpisodes": 100
          }
        },
        {
          "seasonNumber": 2,
          "monitored": false,
          "statistics": {
            "previousAiring": "2016-03-18T04:01:00Z",
            "episodeFileCount": 13,
            "episodeCount": 13,
            "totalEpisodeCount": 13,
            "sizeOnDisk": 56544094360,
            "percentOfEpisodes": 100
          }
        }],
        "year": 2015,
        "path": "F:/TV_Shows/Marvels Daredevil",
        "profileId": 6,
        "seasonFolder": true,
        "monitored": true,
        "useSceneNumbering": false,
        "runtime": 55,
        "tvdbId": 281662,
        "tvRageId": 38796,
        "tvMazeId": 1369,
        "firstAired": "2015-04-10T04:00:00Z",
        "lastInfoSync": "2016-09-09T09:02:49.4402575Z",
        "seriesType": "standard",
        "cleanTitle": "marvelsdaredevil",
        "imdbId": "tt3322312",
        "titleSlug": "marvels-daredevil",
        "certification": "TV-MA",
        "genres": ["Action",
        "Crime",
        "Drama"],
        "tags": [],
        "added": "2015-05-15T00:20:32.7892744Z",
        "ratings": {
          "votes": 461,
          "value": 8.9
        },
        "qualityProfileId": 6,
        "id": 7
    }"""
    )
