"""
This module defines PlayerStatsLegend and PlayerRankedLegend
data class which represents the player's legends stats in the game Brawlhalla.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass, field
from datetime import timedelta

from .player_commons import PlayerCommons

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla


@dataclass
class PlayerStatsLegend:
    """
    PlayerStatsLegend represents a player's legend stats in the game Brawlhalla.
    """

    brawlhalla: Brawlhalla = field(repr=False)
    legend_id: int
    legend_name_key: str
    damagedealt: int
    damagetaken: int
    kos: int
    falls: int
    suicides: int
    teamkos: int
    matchtime: timedelta
    games: int
    wins: int
    damageunarmed: int
    damagethrownitem: int
    damageweaponone: int
    damageweapontwo: int
    damagegadgets: int
    kounarmed: int
    kothrownitem: int
    koweaponone: int
    koweapontwo: int
    kogadgets: int
    timeheldweaponone: timedelta
    timeheldweapontwo: timedelta
    xp: int
    level: int
    xp_percentage: float
    clan: PlayerCommons | None = field(default=None)

    def __init__(
        self,
        brawlhalla: Brawlhalla,
        **kwargs,
    ):
        self.brawlhalla = brawlhalla
        self.__dict__.update(kwargs)
        self.damagedealt = int(kwargs["damagedealt"])
        self.damagetaken = int(kwargs["damagetaken"])
        self.matchtime = timedelta(seconds=kwargs["matchtime"])
        self.damageunarmed = int(kwargs["damageunarmed"])
        self.damagethrownitem = int(kwargs["damagethrownitem"])
        self.damageweaponone = int(kwargs["damageweaponone"])
        self.damageweapontwo = int(kwargs["damageweapontwo"])
        self.damagegadgets = int(kwargs["damagegadgets"])
        self.timeheldweaponone = timedelta(seconds=kwargs["timeheldweaponone"])
        self.timeheldweapontwo = timedelta(seconds=kwargs["timeheldweapontwo"])


@dataclass
class PlayerRankedLegend(PlayerCommons):
    """
    PlayerRankedLegend represents a player's ranked legend stats in the game Brawlhalla.
    """

    legend_id: int
    legend_name_key: str

    def __init__(
        self,
        brawlhalla,
        **kwargs,
    ):
        super().__init__(brawlhalla, **kwargs)
        self.__dict__.update(kwargs)
