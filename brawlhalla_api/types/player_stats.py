"""
This module defines PlayerStats data class which represents
a player's stats in the game Brawlhalla.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass, field

from .player_clan import PlayerClan
from .player_legend import PlayerStatsLegend

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla
    from brawlhalla_api.types import PlayerClan, Clan


@dataclass
class PlayerStats:
    """
    PlayerStats represents a player's stats in the game Brawlhalla.
    """

    brawlhalla: Brawlhalla = field(repr=False)
    brawlhalla_id: int
    name: str
    xp: int
    level: int
    xp_percentage: float
    games: int
    wins: int
    damagebomb: int
    damagemine: int
    damagespikeball: int
    damagesidekick: int
    hitsnowball: int
    kobomb: int
    komine: int
    kospikeball: int
    kosidekick: int
    kosnowball: int
    legends: list[PlayerStatsLegend] = field(default_factory=list)
    clan: PlayerClan | None = field(default=None)

    def __init__(
        self,
        brawlhalla: Brawlhalla,
        **kwargs,
    ) -> None:
        self.brawlhalla = brawlhalla
        self.__dict__.update(kwargs)

        self.name = self.name.encode("raw_unicode_escape").decode("utf-8")
        self.damagebomb = int(self.damagebomb)
        self.damagemine = int(self.damagemine)
        self.damagespikeball = int(self.damagespikeball)
        self.damagesidekick = int(self.damagesidekick)

        if "legends" in kwargs:
            self.legends = [
                PlayerStatsLegend(brawlhalla, **legend) for legend in kwargs["legends"]
            ]
        if "clan" in kwargs:
            self.clan = PlayerClan(brawlhalla, **kwargs["clan"])

    async def get_clan(self) -> Clan | None:
        """
        Gets the clan of the player.

        :return: An object of type `Clan`,
            containing the player's clan or `None` if the player is not in a clan.
        """
        if self.clan:
            return await self.brawlhalla.get_clan(self.clan.clan_id)
