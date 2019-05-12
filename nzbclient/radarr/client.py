import logging
from typing import Dict, List, Union

from nzbclient.radarr.domain.movie import Movie, MovieSchema
from nzbclient.rest_client import RestClient

logger = logging.getLogger(__name__)

MOVIE_ENDPOINT = "/movie"


class RadarrClient(RestClient):
    movie_schema = MovieSchema()

    def add_movie(self, movie: Movie, add_options: Dict = None) -> Movie:
        """
        Adds a movie to Sonarr with the specified data.

        :param movie: An Movie object
        :param add_options: A dict of the add options
        """

        # Dump the data from the passed in object
        movie_data = self.movie_schema.dump(movie)

        if add_options is not None:
            movie_data["add_options"] = add_options

        result = self._post(path=MOVIE_ENDPOINT, data=movie_data)

        return self.movie_schema.load(result)

    def get_movie(self, movie_id: int = None) -> Union[List[Movie], Movie]:
        """
        Gets the specified Movie by id, or a list of all Movie if no Id specified.

        :param movie_id:
        """

        path = f"{MOVIE_ENDPOINT}/{movie_id}" if movie_id else MOVIE_ENDPOINT

        result = self._get(path=path)

        if isinstance(result, list):
            return [self.movie_schema.load(x) for x in result]
        else:
            return self.movie_schema.load(result)

    def update_movie(self, movie: Movie) -> Movie:
        """
        Updates a movie, recommended to do a GET on a specific movie, and modify the required data

        :param movie: An Movie object
        """

        # Dump the data from the passed in object
        movie_data = self.movie_schema.dump(movie)

        result = self._put(path=MOVIE_ENDPOINT, data=movie_data)

        return self.movie_schema.load(result)

    def delete_movie(self, movie_id: int) -> Dict:
        """
        Deletes a movie by Id.

        :param movie_id: The Id of the movie to delete
        """
        path = f"{MOVIE_ENDPOINT}/{movie_id}" if movie_id else MOVIE_ENDPOINT

        return self._delete(path=path)


if __name__ == "__main__":
    client = RadarrClient("http://server-pc:7878", "7f3c6f54c3b348a583c79524c6bd379e")
    print(client.get_movie(1).title)
