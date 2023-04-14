"""
This module defines SteamUser data class which represents
a steam user in the game Brawlhalla.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla
    from brawlhalla_api.types import PlayerRanked, PlayerStats


@dataclass
class SteamUser:
    """
    SteamUser represents a steam user in the game Brawlhalla.
    """

    brawlhalla: Brawlhalla
    brawlhalla_id: int
    name: str

    def __init__(self, brawlhalla: Brawlhalla, brawlhalla_id: int, name: str) -> None:
        self.brawlhalla = brawlhalla
        self.brawlhalla_id = brawlhalla_id
        self.name = name.encode("raw_unicode_escape").decode("utf-8")

    async def get_ranked(self) -> PlayerRanked | None:
        """
        Get the player's ranked stats
        """
        return await self.brawlhalla.get_ranked(self.brawlhalla_id)

    async def get_stats(self) -> PlayerStats | None:
        """
        Get the player's general stats
        """
        return await self.brawlhalla.get_stats(self.brawlhalla_id)
