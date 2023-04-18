"""
This module defines RankingResult data class which represents
a player search result in the game Brawlhalla.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass, field

from brawlhalla_api.types.regions import Region

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla
    from brawlhalla_api.types import PlayerRanked, PlayerStats


@dataclass
class RankingResult:
    """
    RankingResult represents a player search result in the game Brawlhalla.
    """

    brawlhalla: Brawlhalla = field(repr=False)
    brawlhalla_id: int | None = field(default=None)
    brawlhalla_id_one: int | None = field(default=None)
    brawlhalla_id_two: int | None = field(default=None)
    name: str | None = field(default=None)
    rank: int | None = field(default=None)
    tier: str | None = field(default=None)
    games: int = field(default=0)
    wins: int = field(default=0)
    rating: int | None = field(default=None)
    peak_rating: int = field(default=0)
    best_legend: int | None = field(default=None)
    global_rank: int | None = field(default=None)
    best_legend_games: int | None = field(default=None)
    best_legend_wins: int | None = field(default=None)
    teamname: str | None = field(default=None)
    twitch_name: str | None = field(default=None)
    twitch_name_one: str | None = field(default=None)
    twitch_name_two: str | None = field(default=None)
    region: Region | None = field(default=None)

    def __init__(
        self,
        brawlhalla: Brawlhalla,
        **kwargs,
    ) -> None:
        self.brawlhalla = brawlhalla
        self.__dict__.update(kwargs)

        if isinstance(self.region, str):
            self.region = Region.from_str(self.region)
        if isinstance(self.region, int):
            self.region = Region.from_id(self.region)

        if self.rank:
            self.rank = int(self.rank)
        if self.name:
            self.name = self.name.encode("raw_unicode_escape").decode("utf-8")
        if self.teamname:
            self.teamname = self.teamname.encode("raw_unicode_escape").decode("utf-8")
        if self.twitch_name:
            self.twitch_name = self.twitch_name.encode("raw_unicode_escape").decode(
                "utf-8"
            )
        if self.twitch_name_one:
            self.twitch_name_one = self.twitch_name_one.encode(
                "raw_unicode_escape"
            ).decode("utf-8")
        if self.twitch_name_two:
            self.twitch_name_two = self.twitch_name_two.encode(
                "raw_unicode_escape"
            ).decode("utf-8")

    async def get_ranked(self) -> PlayerRanked | None:
        """
        Gets the ranked information for the player.

        :return: An object of type `PlayerRanked`, containing the player's ranked information.
        """
        if self.brawlhalla_id:
            return await self.brawlhalla.get_ranked(self.brawlhalla_id)

    async def get_stats(self) -> PlayerStats | None:
        """
        Gets the overall statistics for the player.

        :return: An object of type `PlayerStats`, containing the player's overall statistics.
        """
        if self.brawlhalla_id:
            return await self.brawlhalla.get_stats(self.brawlhalla_id)
