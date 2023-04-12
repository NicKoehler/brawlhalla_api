"""
This module defines RankingResult data class which represents
a player search result in the game Brawlhalla.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from brawlhalla_api.types.regions import Region


if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla
    from brawlhalla_api.types import PlayerRanked, PlayerStats


class RankingResult:
    """
    RankingResult represents a player search result in the game Brawlhalla.
    """

    def __init__(
        self,
        brawlhalla: Brawlhalla,
        **kwargs,
    ) -> None:
        self.brawlhalla = brawlhalla
        self.brawlhalla_id = kwargs.get("brawlhalla_id")
        self.brawlhalla_id_one = kwargs.get("brawlhalla_id_one")
        self.brawlhalla_id_two = kwargs.get("brawlhalla_id_two")
        self.name = kwargs.get("name")
        self.rank = kwargs.get("rank")
        self.tier = kwargs.get("tier")
        self.games = kwargs.get("games")
        self.wins = kwargs.get("wins")
        self.rating = kwargs.get("rating")
        self.peak_rating = kwargs.get("peak_rating")
        self.best_legend = kwargs.get("best_legend")
        self.global_rank = kwargs.get("global_rank")
        self.best_legend_games = kwargs.get("best_legend_games")
        self.best_legend_wins = kwargs.get("best_legend_wins")
        self.teamname = kwargs.get("teamname")
        self.twitch_name = kwargs.get("twitch_name")
        self.twitch_name_one = kwargs.get("twitch_name_one")
        self.twitch_name_two = kwargs.get("twitch_name_two")

        if isinstance(kwargs.get("region"), str):
            self.region = Region.from_str(kwargs.get("region"))
        if isinstance(kwargs.get("region"), int):
            self.region = Region.from_id(kwargs.get("region"))

        if self.rank:
            self.rank = int(self.rank)

        if self.name:
            self.name.encode("raw_unicode_escape").decode("utf-8")
        if self.teamname:
            self.teamname.encode("raw_unicode_escape").decode("utf-8")
        if self.twitch_name:
            self.twitch_name.encode("raw_unicode_escape").decode("utf-8")
        if self.twitch_name_one:
            self.twitch_name_one.encode("raw_unicode_escape").decode("utf-8")
        if self.twitch_name_two:
            self.twitch_name_two.encode("raw_unicode_escape").decode("utf-8")

    async def get_ranked(self) -> PlayerRanked:
        """
        Gets the ranked information for the player.

        :return: An object of type `PlayerRanked`, containing the player's ranked information.
        """
        return await self.brawlhalla.get_ranked(self.brawlhalla_id)

    async def get_stats(self) -> PlayerStats:
        """
        Gets the overall statistics for the player.

        :return: An object of type `PlayerStats`, containing the player's overall statistics.
        """
        return await self.brawlhalla.get_stats(self.brawlhalla_id)
