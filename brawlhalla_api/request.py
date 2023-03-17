from requests import get
from httpx import AsyncClient
from .types.errors import error_checker

BASE_URL = "https://api.brawlhalla.com/"


class Request:
    def __init__(self, api_key) -> None:
        self._base_params = {"api_key": api_key}
        self.session = AsyncClient()

    async def get(self, endpoint, params=None, **kwargs) -> dict:
        if params is None:
            params = self._base_params
        else:
            params = {**self._base_params, **params}
        resp = await self.session.get(BASE_URL + endpoint, params=params, **kwargs)
        data = resp.json()
        error_checker(resp.status_code, data)
        return data


class RequestSync(Request):
    def __init__(self, api_key) -> None:
        super().__init__(api_key)

    def get(self, endpoint, params=None, **kwargs) -> dict:
        if params is None:
            params = self._base_params
        else:
            params = {**self._base_params, **params}

        resp = get(BASE_URL + endpoint, params=params, **kwargs)
        data = resp.json()
        error_checker(resp.status_code, data)
        return data
