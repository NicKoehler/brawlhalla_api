from .base import Base
from .ranking_result import RankingResult
from .player_legend import PlayerRankedLegend


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
        super().__init__(brawlhalla)
