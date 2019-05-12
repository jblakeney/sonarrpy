from nzbclient.nzbdrone.sonarr.domain.profile import ProfileSchema


def test_profile_serialization(profile_json):
    schema = ProfileSchema()
    results = [schema.load(x) for x in profile_json]

    # TODO: Add more validation here
    assert len(results) == 4
    assert results[2].name == "HD 1080p"
    assert results[2].cutoff.id == 9
    assert results[2].cutoff.name == "HDTV-1080p"
    assert len(results[2].items) == 10


def test_profile_deserialization(profile_obj):
    schema = ProfileSchema()
    results = [schema.dump(x) for x in profile_obj]

    # TODO: Add more validation here
    assert len(results) == 4
    assert results[2].get("name") == "HD 1080p"
    assert results[2].get("cutoff").get("id") == 9
    assert results[2].get("cutoff").get("name") == "HDTV-1080p"
    assert len(results[2].get("items")) == 10
