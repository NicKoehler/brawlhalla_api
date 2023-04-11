from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime
from dataclasses import dataclass

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla


@dataclass
class ClanComponent:
    def __init__(
        self,
        brawlhalla: Brawlhalla,
        **kwargs,
    ) -> None:
        self.brawlhalla = brawlhalla
        self.brawlhalla_id = kwargs.get("brawlhalla_id")
        self.name = kwargs.get("name").encode("raw_unicode_escape").decode("utf-8")
        self.rank = kwargs.get("rank")
        self.join_date = datetime.fromtimestamp(kwargs.get("join_date"))
        self.xp = kwargs.get("xp")


@dataclass
class Clan:
    def __init__(
        self,
        brawlhalla: Brawlhalla,
        **kwargs,
    ) -> None:
        self.brawlhalla = brawlhalla
        self.clan_id = kwargs.get("clan_id")
        self.clan_name = (
            kwargs.get("clan_name").encode("raw_unicode_escape").decode("utf-8")
        )
        self.clan_create_date = datetime.fromtimestamp(kwargs.get("clan_create_date"))
        self.clan_xp = kwargs.get("clan_xp")
        self.components = [
            ClanComponent(brawlhalla, **component) for component in kwargs.get("clan")
        ]
