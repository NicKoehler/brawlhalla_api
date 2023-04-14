"""
This module contains two data classes,
ClanComponent and Clan, which represent the
components of a clan.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass, field
from datetime import datetime as dt

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla


@dataclass
class ClanComponent:
    """

    ClanComponent represents an individual player's data within a clan,
    and contains the following attributes:

    brawlhalla: an instance of the Brawlhalla class
    brawlhalla_id: the player's unique Brawlhalla ID
    name: the player's in-game name
    rank: the player's rank within the clan
    join_date: the date the player joined the clan
    xp: the player's XP within the clan
    """

    brawlhalla: Brawlhalla = field(repr=False)
    name: str
    rank: str
    join_date: dt
    xp: int

    def __init__(
        self,
        brawlhalla: Brawlhalla,
        **kwargs,
    ) -> None:
        self.brawlhalla = brawlhalla
        self.__dict__.update(kwargs)
        self.name = self.name.encode("raw_unicode_escape").decode("utf-8")
        if "join_date" in kwargs:
            self.join_date = dt.fromtimestamp(kwargs["join_date"])


@dataclass
class Clan:
    """
    Clan represents the entire clan, and contains the following attributes:

    brawlhalla: an instance of the Brawlhalla class
    clan_id: the clan's unique ID
    clan_name: the clan's name
    clan_create_date: the date the clan was created
    clan_xp: the clan's total XP
    components: a list of ClanComponent instances representing each player in the clan
    """

    brawlhalla: Brawlhalla = field(repr=False)
    clan_id: int
    clan_name: str
    clan_create_date: dt
    clan_xp: int

    def __init__(
        self,
        brawlhalla: Brawlhalla,
        **kwargs,
    ) -> None:
        self.brawlhalla = brawlhalla
        self.__dict__.update(kwargs)
        self.clan_name = self.clan_name.encode("raw_unicode_escape").decode("utf-8")

        if "clan_create_date" in kwargs:
            self.clan_create_date = dt.fromtimestamp(kwargs["clan_create_date"])
        self.clan_xp = int(self.clan_xp)

        if "clan" in kwargs:
            self.components = [
                ClanComponent(brawlhalla, **component) for component in kwargs["clan"]
            ]
