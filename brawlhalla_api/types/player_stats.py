from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla, BrawlhallaSync
    from brawlhalla_api.types import Clan

from .base import Base
from .player_clan import PlayerClan
from .player_legend import PlayerStatsLegend


class PlayerStats(Base):
    def __init__(
        self,
        brawlhalla: Brawlhalla | BrawlhallaSync,
        brawlhalla_id: int = None,
        name: str = None,
        xp: int = None,
        level: int = None,
        xp_percentage: float = None,
        games: int = None,
        wins: int = None,
        damagebomb: str = None,
        damagemine: str = None,
        damagespikeball: str = None,
        damagesidekick: str = None,
        hitsnowball: int = None,
        kobomb: int = None,
        komine: int = None,
        kospikeball: int = None,
        kosidekick: int = None,
        kosnowball: int = None,
        legends: int = None,
        clan: int = None,
    ) -> None:
        self.brawlhalla_id = brawlhalla_id
        self.name = name
        self.xp = xp
        self.level = level
        self.xp_percentage = xp_percentage
        self.games = games
        self.wins = wins
        self.damagebomb = damagebomb
        self.damagemine = damagemine
        self.damagespikeball = damagespikeball
        self.damagesidekick = damagesidekick
        self.hitsnowball = hitsnowball
        self.kobomb = kobomb
        self.komine = komine
        self.kospikeball = kospikeball
        self.kosidekick = kosidekick
        self.kosnowball = kosnowball
        self.legends = [PlayerStatsLegend(brawlhalla, **legend) for legend in legends]
        self.clan = PlayerClan(brawlhalla, **clan)
        super().__init__(brawlhalla)

    async def get_clan(self) -> Clan | None:
        """
        Gets the clan of the player.

        :return: An object of type `Clan`, containing the player's clan or `None` if the player is not in a clan.
        """
        if self.clan is None:
            return

        return await self.brawlhalla.get_clan(self.clan.clan_id)

    def get_clan(self) -> Clan | None:
        """
        Gets the clan of the player.

        :return: An object of type `Clan`, containing the player's clan or `None` if the player is not in a clan.
        """
        if self.clan is None:
            return

        return self.brawlhalla.get_clan(self.clan.clan_id)
