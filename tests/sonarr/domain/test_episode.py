from datetime import date, datetime

from nzbclients.nzbdrone.sonarr.domain.episode import EpisodeSchema


def test_episode_serialization(episode_json):
    schema = EpisodeSchema()
    result = schema.load(episode_json)

    assert result.series_id == 1
    assert result.episode_file_id == 0
    assert result.season_number == 1
    assert result.episode_number == 1
    assert result.title == "Mole Hunt"
    assert result.air_date == date(2009, 9, 17)
    assert result.air_date_utc == datetime(2009, 9, 18, 2)
    assert len(result.overview) == 312
    assert result.has_file is False
    assert result.monitored is True
    assert result.scene_episode_number == 0
    assert result.scene_season_number == 0
    assert result.tv_db_episode_id == 0
    assert result.absolute_episode_number == 1
    assert result.id == 1


def test_episode_deserialization(episode_obj):
    schema = EpisodeSchema()
    result = schema.dump(episode_obj)

    assert result.get("seriesId") == 1
    assert result.get("episodeFileId") == 0
    assert result.get("seasonNumber") == 1
    assert result.get("episodeNumber") == 1
    assert result.get("title") == "Mole Hunt"
    assert result.get("airDate") == "2009-09-17"
    assert result.get("airDateUtc") == "2009-09-18T02:00:00Z"
    assert len(result.get("overview")) == 312
    assert result.get("hasFile") is False
    assert result.get("monitored") is True
    assert result.get("sceneEpisodeNumber") == 0
    assert result.get("sceneSeasonNumber") == 0
    assert result.get("tvDbEpisodeId") == 0
    assert result.get("absoluteEpisodeNumber") == 1
    assert result.get("id") == 1
