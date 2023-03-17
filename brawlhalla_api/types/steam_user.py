from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla, BrawlhallaSync
    from brawlhalla_api.types import PlayerRanked, PlayerStats

from .base import Base


class SteamUser(Base):
    def __init__(
        self, brawlhalla: Brawlhalla | BrawlhallaSync, brawlhalla_id: int, name: str
    ) -> None:
        self.brawlhalla_id = brawlhalla_id
        self.name = name
        super().__init__(brawlhalla)

    async def get_ranked(self) -> PlayerRanked:
        return await self.brawlhalla.get_ranked(self.brawlhalla_id)

    def get_ranked(self) -> PlayerRanked:
        return self.brawlhalla.get_ranked(self.brawlhalla_id)

    async def get_stats(self) -> PlayerStats:
        return await self.brawlhalla.get_stats(self.brawlhalla_id)

    def get_stats(self) -> PlayerStats:
        return self.brawlhalla.get_stats(self.brawlhalla_id)
