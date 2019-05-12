from typing import List
from datetime import datetime

from marshmallow import Schema, fields

from nzbclient.sonarr.domain.common import SonarrDateTime


class DiskSpace(object):
    def __init__(
        self,
        path: str = None,
        label: str = None,
        free_space: int = None,
        total_space: int = None,
    ):
        self.path = path
        self.label = label
        self.free_space = free_space
        self.total_space = total_space


class RootFolder(object):
    def __init__(
        self,
        path: str = None,
        free_space: int = None,
        unmapped_folders: List = None,
        id: int = None,
    ):
        self.path = path
        self.free_space = free_space
        self.unmapped_folders = unmapped_folders
        self.id = id


class SystemStatus(object):
    def __init__(
        self,
        version: str = None,
        build_time: datetime = None,
        is_debug: bool = None,
        is_production: bool = None,
        is_admin: bool = None,
        is_user_interactive: bool = None,
        startup_path: str = None,
        app_data: str = None,
        os_version: str = None,
        is_mono: bool = None,
        is_linux: bool = None,
        is_windows: bool = None,
        branch: str = None,
        authentication: bool = None,
        start_of_week: int = None,
        url_base: str = None,
    ):
        self.version = version
        self.build_time = build_time
        self.is_debug = is_debug
        self.is_production = is_production
        self.is_admin = is_admin
        self.is_user_interactive = is_user_interactive
        self.startup_path = startup_path
        self.app_data = app_data
        self.os_version = os_version
        self.is_mono = is_mono
        self.is_linux = is_linux
        self.is_windows = is_windows
        self.branch = branch
        self.authentication = authentication
        self.start_of_week = start_of_week
        self.url_base = url_base


class DiskSpaceSchema(Schema):
    class Meta:
        unknown = "EXCLUDE"
        allow_none = False

    path = fields.Str()
    label = fields.Str()
    free_space = fields.Int(data_key="freeSpace")
    total_space = fields.Int(data_key="totalSpace")

    def load(self, data, many=None, partial=None, unknown=None) -> DiskSpace:
        obj = super(Schema, self).load(data, many, partial, unknown)

        return DiskSpace(**obj)


class RootFolderSchema(Schema):
    class Meta:
        unknown = "EXCLUDE"
        allow_none = False

    path = fields.Str()
    free_space = fields.Int(data_key="freeSpace")
    unmapped_folders = fields.List(fields.Str(), data_key="unmappedFolders")
    id = fields.Int()

    def load(self, data, many=None, partial=None, unknown=None) -> RootFolder:
        obj = super(Schema, self).load(data, many, partial, unknown)

        return RootFolder(**obj)


class SystemStatusSchema(Schema):
    class Meta:
        unknown = "EXCLUDE"
        allow_none = False

    version = fields.Str()
    build_time = SonarrDateTime(data_key="buildTime")
    is_debug = fields.Bool(data_key="isDebug")
    is_production = fields.Bool(data_key="isProduction")
    is_admin = fields.Bool(data_key="isAdmin")
    is_user_interactive = fields.Bool(data_key="isUserInteractive")
    startup_path = fields.Str(data_key="startupPath")
    app_data = fields.Str(data_key="appData")
    os_version = fields.Str(data_key="osVersion")
    is_mono = fields.Bool(data_key="isMono")
    is_linux = fields.Bool(data_key="isLinux")
    is_windows = fields.Bool(data_key="isWindows")
    branch = fields.Str()
    authentication = fields.Bool()
    start_of_week = fields.Int(data_key="startOfWeek")
    url_base = fields.Str(data_key="urlBase")

    def load(self, data, many=None, partial=None, unknown=None) -> SystemStatus:
        obj = super(Schema, self).load(data, many, partial, unknown)

        return SystemStatus(**obj)
