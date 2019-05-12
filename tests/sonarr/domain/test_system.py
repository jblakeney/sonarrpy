from nzbclient.sonarr.domain.system import (
    DiskSpaceSchema,
    RootFolderSchema,
    SystemStatusSchema,
)


def test_disk_space_serialization(disk_space_json):
    schema = DiskSpaceSchema()
    result = schema.load(disk_space_json)

    assert result.path == "C:\\"
    assert result.label == ""
    assert result.free_space == 282500067328
    assert result.total_space == 499738734592


def test_disk_space_deserialization(disk_space_obj):
    schema = DiskSpaceSchema()
    result = schema.dump(disk_space_obj)

    assert result.get("path") == "C:\\"
    assert result.get("label") == ""
    assert result.get("freeSpace") == 282500067328
    assert result.get("totalSpace") == 499738734592
