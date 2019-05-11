import logging
from typing import Dict

import requests

logger = logging.getLogger(__name__)


class RestClient(object):
    default_headers = {"Content-Type": "application/json", "Accept": "application/json"}

    def __init__(self, url: str, api_key: str, api_root: str = "api"):
        self._url = url
        self._api_key = api_key
        self._api_root = api_root

        self._session = requests.Session()

    def _construct_url(self, path: str) -> str:
        return f"{self._url}/{self._api_root}{path}?apikey={self._api_key}"

    def _delete(self, path: str) -> Dict:
        return self._send(method="DELETE", path=path)

    def _get(self, path: str) -> Dict:
        return self._send(method="GET", path=path)

    def _put(self, path: str, data: dict) -> Dict:
        return self._send(method="PUT", path=path, data=data)

    def _post(self, path: str, data: dict) -> Dict:
        return self._send(method="POST", path=path, data=data)

    def _send(self, method: str = "GET", path: str = "/", data: dict = None) -> Dict:
        url = self._construct_url(path)

        response = self._session.request(
            method=method, url=url, json=data, headers=self.default_headers, timeout=60
        )

        try:
            if response.text:
                response_content = response.json()
            else:
                response_content = response.content
        except ValueError:
            response_content = response.content

        if response.status_code == 200:
            logger.debug(
                "Received: {0}\n {1}".format(response.status_code, response_content)
            )
        elif response.status_code == 201:
            logger.debug(
                'Received: {0}\n "Created" response'.format(response.status_code)
            )
        elif response.status_code == 204:
            logger.debug(
                'Received: {0}\n "No Content" response'.format(response.status_code)
            )
        elif response.status_code == 401:
            logger.error(
                'Received: {0}\n "UNAUTHORIZED" response'.format(response.status_code)
            )
        elif response.status_code == 404:
            logger.error("Received: {0}\n Not Found".format(response.status_code))
        else:
            response.raise_for_status()

        return response_content
