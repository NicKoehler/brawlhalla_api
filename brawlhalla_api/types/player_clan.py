from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla, BrawlhallaSync

from .base import Base


class PlayerClan(Base):
    def __init__(
        self,
        brawlhalla: Brawlhalla | BrawlhallaSync,
        clan_name: str = None,
        clan_id: int = None,
        clan_xp: int = None,
        personal_xp: int = None,
    ) -> None:
        self.clan_name = clan_name
        self.clan_id = clan_id
        self.clan_xp = int(clan_xp)
        self.personal_xp = personal_xp
        super().__init__(brawlhalla)
