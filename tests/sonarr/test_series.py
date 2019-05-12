import pytest

from marshmallow import ValidationError

from nzbclient.sonarr.series import SeriesSchema


def test_series_serialization(series_json):
    schema = SeriesSchema()
    result = schema.load(series_json)

    # TODO: Test some fields, add more later
    assert result.title == "Marvel's Daredevil"
    assert result.title_slug == "marvels-daredevil"
    assert result.quality_profile_id == 6
    assert result.tvdb_id == 281662


def test_series_deserialization(series_obj):
    schema = SeriesSchema()
    result = schema.dump(series_obj)

    # TODO: Test some fields, add more later
    assert result.get("title") == "Marvel's Daredevil"
    assert result.get("titleSlug") == "marvels-daredevil"
    assert result.get("qualityProfileId") == 6
    assert result.get("tvdbId") == 281662


def test_required_fields():
    schema = SeriesSchema()
    with pytest.raises(ValidationError):
        schema.load({"id": 5})
