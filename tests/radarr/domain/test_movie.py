from nzbclient.nzbdrone.radarr.domain.movie import MovieSchema


def test_movie_serialization(movie_json):
    schema = MovieSchema()
    result = schema.load(movie_json)

    # TODO: Test some fields, add more later
    assert result.title == "Assassin's Creed"
    assert result.title_slug == "assassins-creed-121856"
    assert result.quality_profile_id == 6
    assert result.tmdb_id == 121856


def test_movie_deserialization(movie_obj):
    schema = MovieSchema()
    result = schema.dump(movie_obj)

    # TODO: Test some fields, add more later
    assert result.get("title") == "Assassin's Creed"
    assert result.get("titleSlug") == "assassins-creed-121856"
    assert result.get("qualityProfileId") == 6
    assert result.get("tmdbId") == 121856
