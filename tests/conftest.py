import json
from datetime import datetime

import pytest

from nzbclient import DiskSpace, RootFolder, SystemStatus


@pytest.fixture()
def system_status_obj():
    yield SystemStatus(
        version="2.0.0.1121",
        build_time=datetime(2014, 2, 8, 20, 49, 36, 556039),
        is_debug=False,
        is_production=True,
        is_admin=True,
        is_user_interactive=False,
        startup_path="C:\\ProgramData\\NzbDrone\\bin",
        app_data="C:\\ProgramData\\NzbDrone",
        os_version="6.2.9200.0",
        is_mono=False,
        is_linux=False,
        is_windows=True,
        branch="develop",
        authentication=False,
        start_of_week=0,
        url_base="",
    )


@pytest.fixture()
def system_status_json():
    yield json.loads(
        r"""{
      "version": "2.0.0.1121",
      "buildTime": "2014-02-08T20:49:36.5560392Z",
      "isDebug": false,
      "isProduction": true,
      "isAdmin": true,
      "isUserInteractive": false,
      "startupPath": "C:\\ProgramData\\NzbDrone\\bin",
      "appData": "C:\\ProgramData\\NzbDrone",
      "osVersion": "6.2.9200.0",
      "isMono": false,
      "isLinux": false,
      "isWindows": true,
      "branch": "develop",
      "authentication": false,
      "startOfWeek": 0,
      "urlBase": ""
    }"""
    )


@pytest.fixture()
def disk_space_obj():
    yield [
        DiskSpace(
            path="C:\\", label="", free_space=282500067328, total_space=499738734592
        )
    ]


@pytest.fixture()
def disk_space_json():
    yield json.loads(
        r"""[
           {
              "path":"C:\\",
              "label":"",
              "freeSpace":282500067328,
              "totalSpace":499738734592
           }
        ]"""
    )


@pytest.fixture()
def root_folder_obj():
    yield [
        RootFolder(
            path="C:\\Downloads\\TV", free_space=282500063232, unmapped_folders=[], id=1
        )
    ]


@pytest.fixture()
def root_folder_json():
    yield json.loads(
        r"""[
      {
        "path": "C:\\Downloads\\TV",
        "freeSpace": 282500063232,
        "unmappedFolders": [],
        "id": 1
      }
    ]"""
    )
