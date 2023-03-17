from .request import RequestSync
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


class BrawlhallaSync:
    def __init__(self, api_key: str) -> None:
        self._request = RequestSync(api_key)

    def search(self, steam_id: int | str) -> SteamUser | None:
        """
        Search for a player using their Steam ID.

        :param steam_id: The Steam ID of the player to search for, in the format steamID64 (e.g. 76561198025185087).
        :return: A `SteamUser` object representing the player, or `None` if the player was not found.
        """
        result = self._request.get("search", params={"steamid": steam_id})

        if not result:
            return

        return SteamUser(self, **result)

    def get_rankings(
        self,
        name: str = None,
        bracket: Bracket = Bracket.SINGLE,
        region: Region = Region.ALL,
        page: int | str = 1,
    ) -> list[RankingResult]:
        """
        Get the rankings for a specified bracket, region, and page number.

        :param name: The name of the player to search for in the rankings. If not specified, return all players.
        :param bracket: The bracket to retrieve rankings for, can be one of the values in the `Bracket` enum (SINGLE, DOUBLE, ROTATING).
        :param region: The region to retrieve rankings for, can be one of the values in the `Region` enum (ALL, EU, SEA, BRZ, AUS, US_W, US_E).
        :param page: The page number of the rankings to retrieve. The first page is page 1.
        :return: A list of `RankingResult` objects representing the players in the specified rankings, a empty list if the rankings were not found.

        Note that steam names can change frequently.
        Searching names is currently only implemented for bracket 1v1.
        Searching for a name in 2v2 results in a bad request error response.
        Name searching must start with exact match.
        """
        results = self._request.get(
            f"rankings/{bracket.value}/{region.value}/{page}",
            params={"name": name} if name else None,
        )

        if not results:
            return []

        return [RankingResult(self, **result) for result in results]

    def get_stats(self, brawlhalla_id: int | str) -> PlayerStats | None:
        """
        Get all general stats about a player.

        :param brawlhalla_id: The brawlhalla ID of the player.
        :return: A `PlayerStats` object representing the player, or `None` if the player was not found.
        """
        result = self._request.get(f"player/{brawlhalla_id}/stats")

        if not result:
            return

        return PlayerStats(self, **result)

    def get_ranked(self, brawlhalla_id: int | str) -> PlayerRanked | None:
        """
        Get all ranked stats about a player.

        :param brawlhalla_id: The brawlhalla ID of the player.
        :return: A `PlayerRanked` object representing the player, or `None` if the player was not found.
        """
        result = self._request.get(f"player/{brawlhalla_id}/ranked")

        if not result:
            return

        return PlayerRanked(self, **result)

    def get_clan(self, clan_id: int | str) -> Clan | None:
        """
        Get information about a specific clan and its clan members.

        :param clan_id: The clan ID of a clan.
        :return: A `Clan` object representing the clan, or `None` if the clan was not found.
        """
        result = self._request.get(f"clan/{clan_id}")

        if not result:
            return

        return Clan(self, **result)

    def get_legends(self, legend_id: int | str = "all") -> list[Legend] | LegendDetails:
        """
        Get summarized data for all legends.
        Use the Specific Legend id for more details about a legend.

        The keyword 'all' signifies that every legend should be returned.

        :param legend_id: The legend ID of a legend.
        :return: A `list[Legend]` object of all legends if the keyword 'all' is used,
        a `LegendDetails` object with detauls about a specific legend otherwise.

        Note that calling this method with an invalid legend_id raises `NotFound` exception.

        """
        endpoint = f"legend/{legend_id}"
        if legend_id == "all":
            return [Legend(self, **data) for data in self._request.get(endpoint)]

        return LegendDetails(self, **self._request.get(endpoint))
