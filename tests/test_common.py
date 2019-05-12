from datetime import datetime

from nzbclient.nzbdrone.common import (
    DiskSpaceSchema,
    RootFolderSchema,
    SystemStatusSchema,
)


def test_disk_space_serialization(disk_space_json):
    schema = DiskSpaceSchema()
    results = [schema.load(x) for x in disk_space_json]

    assert len(results) == 1
    assert results[0].path == "C:\\"
    assert results[0].label == ""
    assert results[0].free_space == 282500067328
    assert results[0].total_space == 499738734592


def test_disk_space_deserialization(disk_space_obj):
    schema = DiskSpaceSchema()
    results = [schema.dump(x) for x in disk_space_obj]

    assert len(results) == 1
    assert results[0].get("path") == "C:\\"
    assert results[0].get("label") == ""
    assert results[0].get("freeSpace") == 282500067328
    assert results[0].get("totalSpace") == 499738734592


def test_root_folder_serialization(root_folder_json):
    schema = RootFolderSchema()
    results = [schema.load(x) for x in root_folder_json]

    assert len(results) == 1
    assert results[0].path == "C:\\Downloads\\TV"
    assert results[0].free_space == 282500063232
    assert results[0].unmapped_folders == []
    assert results[0].id == 1


def test_root_folder_deserialization(root_folder_obj):
    schema = RootFolderSchema()
    results = [schema.dump(x) for x in root_folder_obj]

    assert len(results) == 1
    assert results[0].get("path") == "C:\\Downloads\\TV"
    assert results[0].get("freeSpace") == 282500063232
    assert results[0].get("unmappedFolders") == []
    assert results[0].get("id") == 1


def test_system_status_serialization(system_status_json):
    schema = SystemStatusSchema()
    result = schema.load(system_status_json)

    assert result.version == "2.0.0.1121"
    assert result.build_time == datetime(2014, 2, 8, 20, 49, 36, 556039)
    assert result.is_debug is False
    assert result.is_production is True
    assert result.is_admin is True
    assert result.is_user_interactive is False
    assert result.startup_path == "C:\\ProgramData\\NzbDrone\\bin"
    assert result.app_data == "C:\\ProgramData\\NzbDrone"
    assert result.os_version == "6.2.9200.0"
    assert result.is_mono is False
    assert result.is_linux is False
    assert result.is_windows is True
    assert result.branch == "develop"
    assert result.authentication is False
    assert result.start_of_week == 0
    assert result.url_base == ""


def test_system_status_deserialization(system_status_obj):
    schema = SystemStatusSchema()
    result = schema.dump(system_status_obj)

    assert result.get("version") == "2.0.0.1121"
    assert result.get("buildTime") == "2014-02-08T20:49:36Z"
    assert result.get("isDebug") is False
    assert result.get("isProduction") is True
    assert result.get("isAdmin") is True
    assert result.get("isUserInteractive") is False
    assert result.get("startupPath") == "C:\\ProgramData\\NzbDrone\\bin"
    assert result.get("appData") == "C:\\ProgramData\\NzbDrone"
    assert result.get("osVersion") == "6.2.9200.0"
    assert result.get("isMono") is False
    assert result.get("isLinux") is False
    assert result.get("isWindows") is True
    assert result.get("branch") == "develop"
    assert result.get("authentication") is False
    assert result.get("startOfWeek") == 0
    assert result.get("urlBase") == ""
