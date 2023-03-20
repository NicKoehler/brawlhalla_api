from .base import Base
from .ranking_result import RankingResult
from .player_legend import PlayerRankedLegend
from .. import utils


class PlayerRanked(Base):
    def __init__(
        self,
        brawlhalla,
        name: str = None,
        brawlhalla_id: int = None,
        rating: int = None,
        peak_rating: int = None,
        tier: str = None,
        wins: int = None,
        games: int = None,
        region: str = None,
        global_rank: int = None,
        region_rank: int = None,
        legends: PlayerRankedLegend = [],
        **kwargs
    ) -> None:
        self.name = name
        self.brawlhalla_id = brawlhalla_id
        self.rating = rating
        self.peak_rating = peak_rating
        self.tier = tier
        self.wins = wins
        self.games = games
        self.region = region
        self.global_rank = global_rank
        self.region_rank = region_rank
        self.legends = [PlayerRankedLegend(brawlhalla, **legend) for legend in legends]
        self.teams = [RankingResult(brawlhalla, **team) for team in kwargs["2v2"]]
        self.estimated_glory = self._get_glory()
        self.estimated_elo_reset = utils.get_personal_elo_from_old_elo(self.rating)
        super().__init__(brawlhalla)

    def _get_glory(self) -> int:
        peak_rating = self.peak_rating
        total_wins = self.wins

        for elem in self.teams + self.legends:
            total_wins += elem.wins
            if elem.peak_rating > peak_rating:
                peak_rating = elem.peak_rating

        glory_wins = utils.get_glory_from_wins(total_wins)
        glory_rating = utils.get_glory_from_best_rating(peak_rating)

        return glory_rating + glory_wins
