import logging
from typing import Dict, List, Union

from sonarrpy.rest_client import RestClient

logger = logging.getLogger(__name__)

DISKSPACE_ENDPOINT = "/diskspace"
EPISODE_ENDPOINT = "/episode"
PROFILE_ENDPOINT = "/profile"
SERIES_ENDPOINT = "/series"
SYSTEM_STATUS_ENDPOINT = "/system/status"


class SonarrClient(RestClient):
    def get_diskspace(self) -> List[Dict]:
        """
        Gets the information on the diskspace of the configured drives
        """
        return self._get(DISKSPACE_ENDPOINT)

    def get_system_status(self) -> Dict:
        """
        Gets the system status from the Sonarr server
        """
        return self._get(SYSTEM_STATUS_ENDPOINT)

    def get_profile(self) -> List[Dict]:
        """
        Gets a list of all available quality profiles
        """
        return self._get(PROFILE_ENDPOINT)

    def get_episode(self, episode_id: int = None, series_id: int = None):
        """
        Gets the specified Episode by either Series Id, or Episode Id. Only one should be specifeid

        :param episode_id:
        :param series_id:
        """
        params = {}
        path = EPISODE_ENDPOINT
        if series_id and episode_id:
            raise ValueError(
                "Only one of Episode Id or Series Id can be specified, not both."
            )
        elif episode_id:
            path += f"/{episode_id}"
        elif series_id:
            params["seriesId"] = series_id
        else:
            raise ValueError("One of Episode Id or Series Id must be specified.")

        return self._get(path, params=params)

    def update_episode(self, episode_data: dict) -> Dict:
        """
        Updates a episode, recommended to do a GET on a specific episode, and modify the required data

        :param episode_data: The entire dict of the Episode data
        """
        return self._put(EPISODE_ENDPOINT, episode_data)

    def add_series(
        self,
        title: str,
        title_slug: str,
        tvdb_id: int,
        quality_profile_id: int,
        path: str,
        images: List[Dict] = None,
        seasons: List[Dict] = None,
        season_folder: bool = False,
        monitored: bool = False,
        add_options: Dict = None,
    ) -> Dict:
        """
        Adds a series to Sonarr with the specified data.

        :param title: Title of the series
        :param title_slug: A slug version of the title
        :param tvdb_id: Valid TVDB Id
        :param quality_profile_id: The Id of the Quality Profile to use
        :param path: The full path to store the Series on the Sonarr server
        :param images: A list of custom image objects
        :param seasons: A list of seasons
        :param season_folder:
        :param monitored: Flag the Series as monitored
        :param add_options: Optional list of options when adding the Series
        """
        # Create the data with the required params
        series_data = {
            "title": title,
            "titleSlug": title_slug,
            "tvdbId": tvdb_id,
            "qualityProfileId": quality_profile_id,
            "path": path,
            "images": images or [],
            "seasons": seasons or [],
            "seasonFolder": season_folder,
            "monitored": monitored,
        }

        # Add all optional data if specified
        if add_options is not None:
            series_data["add_options"] = add_options

        return self._post(SERIES_ENDPOINT, series_data)

    def get_series(self, series_id: int = None) -> Union[List[Dict], Dict]:
        """
        Gets the specified Series by id, or a list of all Series if no Id specified.

        :param series_id:
        """

        path = f"{SERIES_ENDPOINT}/{series_id}" if series_id else SERIES_ENDPOINT

        return self._get(path)

    def update_series(self, series_data: dict) -> Dict:
        """
        Updates a series, recommended to do a GET on a specific series, and modify the required data

        :param series_data: The entire dict of the Series data
        """
        return self._put(SERIES_ENDPOINT, series_data)

    def delete_series(self, series_id: int) -> Dict:
        """
        Deletes a series by Id.

        :param series_id: The Id of the series to delete
        """
        path = f"{SERIES_ENDPOINT}/{series_id}" if series_id else SERIES_ENDPOINT

        return self._delete(path)
