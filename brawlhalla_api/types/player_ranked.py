"""
This module defines PlayerRanked data class which represents
a ranked player in the game Brawlhalla.

"""
from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass

from .. import utils
from .regions import Region
from .ranking_result import RankingResult
from .player_legend import PlayerRankedLegend
from .player_commons import PlayerCommons

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla


@dataclass
class PlayerRanked(PlayerCommons):
    """
    PlayerRanked represents a ranked player in the game Brawlhalla.
    """

    name: str
    brawlhalla_id: int
    region: Region | None
    global_rank: int
    region_rank: int
    legends: list[PlayerRankedLegend]
    teams: list[RankingResult]
    rotating_ranked: RankingResult | None

    def __init__(self, brawlhalla: Brawlhalla, **kwargs) -> None:
        super().__init__(brawlhalla, **kwargs)
        self.__dict__.update(kwargs)
        self.name = self.name.encode("raw_unicode_escape").decode("utf-8")

        if "legends" in kwargs:
            self.legends = [
                PlayerRankedLegend(brawlhalla, **legend) for legend in kwargs["legends"]
            ]
        if "2v2" in kwargs:
            self.teams = [RankingResult(brawlhalla, **team) for team in kwargs["2v2"]]

        if "rotating_ranked" in kwargs:
            rotatings = kwargs["rotating_ranked"]
            if isinstance(rotatings, dict):
                self.rotating_ranked = RankingResult(brawlhalla, **rotatings)

        self.region = (
            Region.from_str(kwargs["region"]) if self.region != "none" else None
        )

        self.estimated_glory = self._get_glory()
        self.estimated_elo_reset = utils.get_personal_elo_from_old_elo(self.rating)

    def _get_glory(self) -> int:
        """
        Returns the player's estimated glory.

        this method is automatically called by the __init__ method.

        """
        total_wins = self.wins
        total_games = self.games
        peak_rating = self.peak_rating

        for elem in self.teams:
            total_wins += elem.wins
            total_games += elem.games
            if elem.peak_rating > peak_rating:
                peak_rating = elem.peak_rating

        for elem in self.legends:
            if elem.peak_rating > peak_rating:
                peak_rating = elem.peak_rating

        if self.rotating_ranked:
            total_wins += self.rotating_ranked.wins
            total_games += self.rotating_ranked.games
            if self.rotating_ranked.peak_rating > peak_rating:
                peak_rating = self.rotating_ranked.peak_rating

        # Sorry, gotta play 10 games!
        if total_games < 10:
            return 0

        glory_wins = utils.get_glory_from_wins(total_wins)
        glory_rating = utils.get_glory_from_best_rating(peak_rating)

        return glory_rating + glory_wins
