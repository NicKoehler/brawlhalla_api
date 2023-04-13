"""
This module defines PlayerRanked data class which represents
a ranked player in the game Brawlhalla.

"""

from dataclasses import dataclass

from .. import utils
from .regions import Region
from .ranking_result import RankingResult
from .player_legend import PlayerRankedLegend
from .player_commons import PlayerCommons


@dataclass
class PlayerRanked(PlayerCommons):
    """
    PlayerRanked represents a ranked player in the game Brawlhalla.
    """

    def __init__(self, brawlhalla, **kwargs) -> None:
        super().__init__(brawlhalla, **kwargs)
        self.name = kwargs.get("name").encode("raw_unicode_escape").decode("utf-8")
        self.brawlhalla_id = kwargs.get("brawlhalla_id")
        self.region = kwargs.get("region")
        self.global_rank = kwargs.get("global_rank")
        self.region_rank = kwargs.get("region_rank")
        self.legends = [
            PlayerRankedLegend(brawlhalla, **legend) for legend in kwargs.get("legends")
        ]
        self.teams = [RankingResult(brawlhalla, **team) for team in kwargs.get("2v2")]
        if isinstance(kwargs.get("rotating_ranked"), list):
            self.rotating_ranked = None
        else:
            self.rotating_ranked = RankingResult(
                brawlhalla, **kwargs.get("rotating_ranked")
            )

        if self.region != "none":
            self.region = Region.from_str(self.region)
        else:
            self.region = None

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
