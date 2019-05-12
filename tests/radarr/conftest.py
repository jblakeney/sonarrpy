import json
from datetime import datetime

import pytest

from nzbclientz.nzbdrone.common import Image, Ratings
from nzbclientz.nzbdrone.radarr.domain.movie import AlternateTitle, Movie


@pytest.fixture()
def movie_obj():
    yield Movie(
        title="Assassin's Creed",
        sort_title="assassins creed",
        size_on_disk=0,
        status="released",
        overview="Lynch discovers he is a descendant of the secret Assassins society through unlocked genetic memories that allow him to relive the adventures of his ancestor, Aguilar, in 15th Century Spain. After gaining incredible knowledge and skills he’s poised to take on the oppressive Knights Templar in the present day.",
        in_cinemas=datetime(2016, 12, 21),
        images=[
            Image(
                cover_type="poster",
                url="/radarr/MediaCover/1/poster.jpg?lastWrite=636200219330000000",
            ),
            Image(
                cover_type="banner",
                url="/radarr/MediaCover/1/banner.jpg?lastWrite=636200219340000000",
            ),
        ],
        website="https://www.ubisoft.com/en-US/",
        downloaded=False,
        year=2016,
        has_file=False,
        you_tube_trailer_id="pgALJgMjXN4",
        studio="20th Century Fox",
        path="/path/to/Assassin's Creed (2016)",
        profile_id=6,
        monitored=True,
        minimum_availability="preDb",
        runtime=115,
        last_info_sync=datetime(2017, 1, 23, 22, 5, 32, 365337),
        clean_title="assassinscreed",
        imdb_id="tt2094766",
        tmdb_id=121856,
        title_slug="assassins-creed-121856",
        genres=["Action", "Adventure", "Fantasy", "Science Fiction"],
        tags=[],
        added=datetime(2017, 1, 14, 20, 18, 52, 938244),
        ratings=Ratings(votes=711, value=5.2),
        alternative_titles=[
            AlternateTitle(title="Assassin's Creed: The IMAX Experience")
        ],
        quality_profile_id=6,
        id=1,
    )


@pytest.fixture()
def movie_json():
    yield json.loads(
        r"""{
      "title": "Assassin's Creed",
      "sortTitle": "assassins creed",
      "sizeOnDisk": 0,
      "status": "released",
      "overview": "Lynch discovers he is a descendant of the secret Assassins society through unlocked genetic memories that allow him to relive the adventures of his ancestor, Aguilar, in 15th Century Spain. After gaining incredible knowledge and skills he’s poised to take on the oppressive Knights Templar in the present day.",
      "inCinemas": "2016-12-21T00:00:00Z",
      "images": [
        {
          "coverType": "poster",
          "url": "/radarr/MediaCover/1/poster.jpg?lastWrite=636200219330000000"
        },
        {
          "coverType": "banner",
          "url": "/radarr/MediaCover/1/banner.jpg?lastWrite=636200219340000000"
        }
      ],
      "website": "https://www.ubisoft.com/en-US/",
      "downloaded": false,
      "year": 2016,
      "hasFile": false,
      "youTubeTrailerId": "pgALJgMjXN4",
      "studio": "20th Century Fox",
      "path": "/path/to/Assassin's Creed (2016)",
      "profileId": 6,
      "monitored": true,
      "minimumAvailability": "preDb",
      "runtime": 115,
      "lastInfoSync": "2017-01-23T22:05:32.365337Z",
      "cleanTitle": "assassinscreed",
      "imdbId": "tt2094766",
      "tmdbId": 121856,
      "titleSlug": "assassins-creed-121856",
      "genres": [
        "Action",
        "Adventure",
        "Fantasy",
        "Science Fiction"
      ],
      "tags": [],
      "added": "2017-01-14T20:18:52.938244Z",
      "ratings": {
        "votes": 711,
        "value": 5.2
      },
      "alternativeTitles": [
        {
          "title": "Assassin's Creed: The IMAX Experience"
        }
      ],
      "qualityProfileId": 6,
      "id": 1
    }"""
    )
