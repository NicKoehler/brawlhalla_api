from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla, BrawlhallaSync
    from brawlhalla_api.types import PlayerRanked, PlayerStats

from .base import Base


class RankingResult(Base):
    def __init__(
        self,
        brawlhalla: Brawlhalla | BrawlhallaSync,
        rank: int = None,
        name: str = None,
        tier: str = None,
        games: int = None,
        wins: int = None,
        rating: int = None,
        region: str = None,
        peak_rating: int = None,
        best_legend: int = None,
        global_rank: int = None,
        brawlhalla_id: int = None,
        brawlhalla_id_one: int = None,
        brawlhalla_id_two: int = None,
        best_legend_games: int = None,
        best_legend_wins: int = None,
        teamname: str = None,
        twitch_name: str = None,
        twitch_name_one: str = None,
        twitch_name_two: str = None,
    ) -> None:
        self.brawlhalla_id = brawlhalla_id
        self.brawlhalla_id_one = brawlhalla_id_one
        self.brawlhalla_id_two = brawlhalla_id_two
        if name:
            self.name = name.encode("raw_unicode_escape").decode("utf-8")
        if rank:
            self.rank = int(rank)
        self.tier = tier
        self.games = games
        self.wins = wins
        self.rating = rating
        self.region = region
        self.peak_rating = peak_rating
        self.best_legend = best_legend
        self.global_rank = global_rank
        self.best_legend_games = best_legend_games
        self.best_legend_wins = best_legend_wins
        if teamname:
            self.teamname = teamname.encode("raw_unicode_escape").decode("utf-8")
        if twitch_name:
            self.twitch_name = twitch_name.encode("raw_unicode_escape").decode("utf-8")
        if twitch_name_one:
            self.twitch_name_one = twitch_name_one.encode("raw_unicode_escape").decode(
                "utf-8"
            )
        if twitch_name_two:
            self.twitch_name_two = twitch_name_two.encode("raw_unicode_escape").decode(
                "utf-8"
            )
        super().__init__(brawlhalla)

    async def get_ranked(self) -> PlayerRanked:
        """
        Gets the ranked information for the player.

        :return: An object of type `PlayerRanked`, containing the player's ranked information.
        """
        return await self.brawlhalla.get_ranked(self.brawlhalla_id)

    def get_ranked(self) -> PlayerRanked:
        """
        Gets the ranked information for the player.

        :return: An object of type `PlayerRanked`, containing the player's ranked information.
        """
        return self.brawlhalla.get_ranked(self.brawlhalla_id)

    async def get_stats(self) -> PlayerStats:
        """
        Gets the overall statistics for the player.

        :return: An object of type `PlayerStats`, containing the player's overall statistics.
        """
        return await self.brawlhalla.get_stats(self.brawlhalla_id)

    def get_stats(self) -> PlayerStats:
        """
        Gets the overall statistics for the player.

        :return: An object of type `PlayerStats`, containing the player's overall statistics.
        """
        return self.brawlhalla.get_stats(self.brawlhalla_id)
