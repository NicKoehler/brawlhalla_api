"""
Brawlhalla API python implementation using syncronous requests.

"""

from .request import Request
from .types import (
    Clan,
    Legend,
    Region,
    Bracket,
    SteamUser,
    PlayerStats,
    PlayerRanked,
    RankingResult,
    LegendDetails,
)


class Brawlhalla:
    """
    The `Brawlhalla` class provides an interface for accessing Brawlhalla API endpoints.
    It allows you to search for players, retrieve their rankings, statistics, and clan information,
    as well as get data for all Brawlhalla legends.

    To use this class, you need to provide a valid Brawlhalla API key.

    The class contains the following methods:

    - `search`: Search for a player using their Steam ID.
    - `get_rankings`: Get the rankings for a specified bracket, region, and page number.
    - `get_stats`: Get all stats about a player.
    - `get_ranked`: Get all ranked stats about a player.
    - `get_clan`: Get information about a specific clan and its clan members.
    - `get_legends`: Get summarized data for all legends or details about a specific legend.

    Note that some methods have specific parameters and behaviors
    that are documented in their respective docstrings.

    Some methods may return `None`, an empty list, or raise exceptions
    if no data is found or if invalid parameters are used.
    """

    def __init__(self, api_key: str) -> None:
        self._request = Request(api_key)

    async def search(self, steam_id: int | str) -> SteamUser | None:
        """
        Search for a player using their Steam ID.

        :param steam_id: The Steam ID of the player to search for, in the format steamID64
            (e.g. 76561198025185087).
        :return: A `SteamUser` representing the player, `None` if the player was not found.
        """
        result = await self._request.get("search", params={"steamid": steam_id})

        if not result:
            return

        return SteamUser(self, **result)

    async def get_rankings(
        self,
        name: str = None,
        bracket: Bracket = Bracket.SINGLE,
        region: Region = Region.ALL,
        page: int | str = 1,
    ) -> list[RankingResult]:
        """
        Get the rankings for a specified bracket, region, and page number.

        :param name: The name of the player to search for in the rankings.
            If not specified, return all players.
        :param bracket: The bracket to retrieve rankings for, can be one of the values in the
            `Bracket` enum (SINGLE, DOUBLE, ROTATING).
        :param region: The region to retrieve rankings for, can be one of the values in the
            `Region` enum (ALL, EU, SEA, BRZ, AUS, US_W, US_E, JPN, ME, SA).
        :param page: The page number of the rankings to retrieve. The first page is page 1.
        :return: A list of `RankingResult`s representing the players,
            a empty list if the rankings were not found.

        Note that steam names can change frequently.
        Searching names is currently only implemented for bracket 1v1.
        Searching for a name in 2v2 results in a bad request error response.
        Name searching must start with exact match.
        """
        results = await self._request.get(
            f"rankings/{bracket.value}/{region.value}/{page}",
            params={"name": name} if name else None,
        )

        if not results:
            return []

        return [RankingResult(self, **result) for result in results]

    async def get_stats(self, brawlhalla_id: int | str) -> PlayerStats | None:
        """
        Get all stats about a player.

        :param brawlhalla_id: The brawlhalla ID of the player.
        :return: A `PlayerStats` representing the player, `None` if the player was not found.
        """
        result = await self._request.get(f"player/{brawlhalla_id}/stats")

        if not result:
            return None

        return PlayerStats(self, **result)

    async def get_ranked(self, brawlhalla_id: int | str) -> PlayerRanked | None:
        """
        Get all ranked stats about a player.

        :param brawlhalla_id: The brawlhalla ID of the player.
        :return: A `PlayerRanked` representing the player, `None` if the player was not found.
        """
        result = await self._request.get(f"player/{brawlhalla_id}/ranked")

        if not result:
            return None

        return PlayerRanked(self, **result)

    async def get_clan(self, clan_id: int | str) -> Clan | None:
        """
        Get information about a specific clan and its clan members.

        :param clan_id: The clan ID of a clan.
        :return: A `Clan` representing the clan, or `None` if the clan was not found.
        """
        result = await self._request.get(f"clan/{clan_id}")

        if not result:
            return None

        return Clan(self, **result)

    async def get_legends(
        self, legend_id: int | str = "all"
    ) -> list[Legend] | LegendDetails:
        """
        Get summarized data for all legends.
        Use the Specific Legend id for more details about a legend.

        The keyword 'all' signifies that every legend should be returned.

        :param legend_id: The legend ID of a legend.
        :return: A `list[Legend]` of all legends if the keyword 'all' is used,
        a `LegendDetails` with detauls about a specific legend otherwise.

        Note that calling this method with an invalid legend_id raises `NotFound` exception.

        """
        endpoint = f"legend/{legend_id}"
        if legend_id == "all":
            return [
                Legend(self, **data) for data in (await self._request.get(endpoint))
            ]

        return LegendDetails(self, **await self._request.get(endpoint))
