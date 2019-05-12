from nzbclient.sonarr.domain.profile import ProfileSchema


def test_profile_serialization(profile_json):
    schema = ProfileSchema()
    results = [schema.load(x) for x in profile_json]

    # TODO: Add more validation here
    assert len(results) == 4


def test_profile_deserialization(profile_obj):
    schema = ProfileSchema()
    results = [schema.dump(x) for x in profile_obj]

    # TODO: Add more validation here
    assert len(results) == 4
