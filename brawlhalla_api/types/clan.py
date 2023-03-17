from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla, BrawlhallaSync


from datetime import datetime
from .base import Base


class ClanComponent(Base):
    def __init__(
        self,
        brawlhalla: Brawlhalla | BrawlhallaSync,
        brawlhalla_id: int = None,
        name: str = None,
        rank: str = None,
        join_date: int = None,
        xp: int = None,
    ) -> None:
        self.brawlhalla_id = brawlhalla_id
        self.name = name.encode("raw_unicode_escape").decode("utf-8")
        self.rank = rank
        self.join_date = datetime.fromtimestamp(join_date)
        self.xp = xp
        super().__init__(brawlhalla)


class Clan(Base):
    def __init__(
        self,
        brawlhalla: Brawlhalla | BrawlhallaSync,
        clan_id: int = None,
        clan_name: str = None,
        clan_create_date: datetime = None,
        clan_xp: str = None,
        **kwargs,
    ) -> None:
        self.clan_id = clan_id
        self.clan_name = clan_name.encode("raw_unicode_escape").decode("utf-8")
        self.clan_create_date = datetime.fromtimestamp(clan_create_date)
        self.clan_xp = clan_xp
        self.components = [
            ClanComponent(brawlhalla, **component) for component in kwargs["clan"]
        ]
        super().__init__(brawlhalla)
