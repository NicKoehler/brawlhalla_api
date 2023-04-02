from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla, BrawlhallaSync

from .base import Base
from datetime import timedelta


class PlayerStatsLegend(Base):
    def __init__(
        self,
        brawlhalla: Brawlhalla | BrawlhallaSync,
        legend_id: int = None,
        legend_name_key: str = None,
        damagedealt: int = None,
        damagetaken: int = None,
        kos: int = None,
        falls: int = None,
        suicides: int = None,
        teamkos: int = None,
        matchtime: int = None,
        games: int = None,
        wins: int = None,
        damageunarmed: int = None,
        damagethrownitem: int = None,
        damageweaponone: int = None,
        damageweapontwo: int = None,
        damagegadgets: int = None,
        kounarmed: int = None,
        kothrownitem: int = None,
        koweaponone: int = None,
        koweapontwo: int = None,
        kogadgets: int = None,
        timeheldweaponone: int = None,
        timeheldweapontwo: int = None,
        xp: int = None,
        level: int = None,
        xp_percentage: float = None,
    ):
        self.legend_id = legend_id
        self.legend_name_key = legend_name_key
        self.damagedealt = int(damagedealt)
        self.damagetaken = int(damagetaken)
        self.kos = kos
        self.falls = falls
        self.suicides = suicides
        self.teamkos = teamkos
        self.matchtime = timedelta(seconds=matchtime) 
        self.games = games
        self.wins = wins
        self.damageunarmed = int(damageunarmed)
        self.damagethrownitem = int(damagethrownitem)
        self.damageweaponone = int(damageweaponone)
        self.damageweapontwo = int(damageweapontwo)
        self.damagegadgets = int(damagegadgets)
        self.kounarmed = kounarmed
        self.kothrownitem = kothrownitem
        self.koweaponone = koweaponone
        self.koweapontwo = koweapontwo
        self.kogadgets = kogadgets
        self.timeheldweaponone = timeheldweaponone
        self.timeheldweapontwo = timeheldweapontwo
        self.xp = xp
        self.level = level
        self.xp_percentage = xp_percentage
        super().__init__(brawlhalla)


class PlayerRankedLegend(Base):
    def __init__(
        self,
        brawlhalla,
        legend_id: int = None,
        legend_name_key: str = None,
        rating: int = None,
        peak_rating: int = None,
        tier: str = None,
        wins: int = None,
        games: int = None,
    ):
        self.legend_id = legend_id
        self.legend_name_key = legend_name_key
        self.rating = rating
        self.peak_rating = peak_rating
        self.tier = tier
        self.wins = wins
        self.games = games
        super().__init__(brawlhalla)
