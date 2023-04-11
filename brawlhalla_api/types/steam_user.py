from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla
    from brawlhalla_api.types import PlayerRanked, PlayerStats


class SteamUser:
    def __init__(self, brawlhalla: Brawlhalla, brawlhalla_id: int, name: str) -> None:
        self.brawlhalla = brawlhalla
        self.brawlhalla_id = brawlhalla_id
        self.name = name

    async def get_ranked(self) -> PlayerRanked:
        return await self.brawlhalla.get_ranked(self.brawlhalla_id)

    async def get_stats(self) -> PlayerStats:
        return await self.brawlhalla.get_stats(self.brawlhalla_id)
