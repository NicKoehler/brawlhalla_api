"""
This module sends GET requests to the Brawlhalla API endpoint
and returns the response data as a dictionary.

It contains a class 'Request' that is used to send an async GET request to the API endpoint
with optional query parameters and returns the response data as a dictionary.

"""
from httpx import AsyncClient
from .errors import error_checker

BASE_URL = "https://api.brawlhalla.com/"


class Request:
    """
    This class is used to send an async GET request to the API endpoint with optional query
    parameters and returns the response data as a dictionary.
    """

    def __init__(self, api_key) -> None:
        self._base_params = {"api_key": api_key}
        self.session = AsyncClient()

    async def get(self, endpoint, params=None, **kwargs) -> dict:
        """
        This function sends a GET request to the API endpoint with optional query
        parameters and returns the response data as a dictionary.
        This function automatically adds the `api_key` query parameter to every request
        and can raise an exception if the api call fails.

        :param endpoint: The endpoint URL to send the GET request to.
        :param params: A dictionary of query parameters to send with the GET request.
        :param kwargs: Additional keyword arguments to send with the GET request.

        :return: The response data as a dictionary.
        """
        if params is None:
            params = self._base_params
        else:
            params = {**self._base_params, **params}
        resp = await self.session.get(
            BASE_URL + endpoint,
            params=params,
            timeout=10,
            **kwargs,
        )
        data = resp.json()
        error_checker(resp.status_code, data)
        return data
