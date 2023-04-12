"""
This module defines PlayerStatsLegend and PlayerRankedLegend
data class which represents the player's legends stats in the game Brawlhalla.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass
from datetime import timedelta
from .player_commons import PlayerCommons

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla


@dataclass
class PlayerStatsLegend:
    """
    PlayerStatsLegend represents a player's legend stats in the game Brawlhalla.
    """

    def __init__(
        self,
        brawlhalla: Brawlhalla,
        **kwargs,
    ):
        self.brawlhalla = brawlhalla
        self.legend_id = kwargs.get("legend_id")
        self.legend_name_key = kwargs.get("legend_name_key")
        self.damagedealt = int(kwargs.get("damagedealt"))
        self.damagetaken = int(kwargs.get("damagetaken"))
        self.kos = kwargs.get("kos")
        self.falls = kwargs.get("falls")
        self.suicides = kwargs.get("suicides")
        self.teamkos = kwargs.get("teamkos")
        self.matchtime = timedelta(seconds=kwargs.get("matchtime"))
        self.games = kwargs.get("games")
        self.wins = kwargs.get("wins")
        self.damageunarmed = int(kwargs.get("damageunarmed"))
        self.damagethrownitem = int(kwargs.get("damagethrownitem"))
        self.damageweaponone = int(kwargs.get("damageweaponone"))
        self.damageweapontwo = int(kwargs.get("damageweapontwo"))
        self.damagegadgets = int(kwargs.get("damagegadgets"))
        self.kounarmed = kwargs.get("kounarmed")
        self.kothrownitem = kwargs.get("kothrownitem")
        self.koweaponone = kwargs.get("koweaponone")
        self.koweapontwo = kwargs.get("koweapontwo")
        self.kogadgets = kwargs.get("kogadgets")
        self.timeheldweaponone = timedelta(seconds=kwargs.get("timeheldweaponone"))
        self.timeheldweapontwo = timedelta(seconds=kwargs.get("timeheldweapontwo"))
        self.xp = kwargs.get("xp")
        self.level = kwargs.get("level")
        self.xp_percentage = kwargs.get("xp_percentage")


@dataclass
class PlayerRankedLegend(PlayerCommons):
    """
    PlayerRankedLegend represents a player's ranked legend stats in the game Brawlhalla.
    """

    def __init__(
        self,
        brawlhalla,
        **kwargs,
    ):
        super().__init__(brawlhalla, **kwargs)
        self.legend_id = kwargs.get("legend_id")
        self.legend_name_key = kwargs.get("legend_name_key")
