import logging
from typing import Dict, List, Union

from nzbclient.rest_client import RestClient
from nzbclient.sonarr.series import Series, SeriesSchema

logger = logging.getLogger(__name__)

DISKSPACE_ENDPOINT = "/diskspace"
EPISODE_ENDPOINT = "/episode"
PROFILE_ENDPOINT = "/profile"
SERIES_ENDPOINT = "/series"
SYSTEM_STATUS_ENDPOINT = "/system/status"


class SonarrClient(RestClient):
    series_schema = SeriesSchema()

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

    def add_series(self, series: Series, add_options: Dict = None) -> Series:
        """
        Adds a series to Sonarr with the specified data.

        :param series: A Series object
        :param add_options: A dict of the add options
        """

        # Dump the data from the passed in object
        series_data = self.series_schema.dump(series)

        if add_options is not None:
            series_data["add_options"] = add_options

        result = self._post(path=SERIES_ENDPOINT, data=series_data)

        return self.series_schema.load(result)

    def get_series(self, series_id: int = None) -> Union[List[Series], Series]:
        """
        Gets the specified Series by id, or a list of all Series if no Id specified.

        :param series_id:
        """

        path = f"{SERIES_ENDPOINT}/{series_id}" if series_id else SERIES_ENDPOINT

        result = self._get(path)

        if isinstance(result, list):
            return [self.series_schema.load(x) for x in result]
        else:
            return self.series_schema.load(result)

    def update_series(self, series: Series) -> Series:
        """
        Updates a series, recommended to do a GET on a specific series, and modify the required data

        :param series: A Series object
        """

        # Dump the data from the passed in object
        series_data = self.series_schema.dump(series)

        result = self._put(SERIES_ENDPOINT, series_data)

        return self.series_schema.load(result)

    def delete_series(self, series_id: int) -> Dict:
        """
        Deletes a series by Id.

        :param series_id: The Id of the series to delete
        """
        path = f"{SERIES_ENDPOINT}/{series_id}" if series_id else SERIES_ENDPOINT

        return self._delete(path)


if __name__ == "__main__":
    client = SonarrClient("http://server-pc:8989", "49095f567f67413cb5956f8032950f7e")
    print(client.get_series(1))
