"""
This module contains two data classes,
ClanComponent and Clan, which represent the
components of a clan.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime
from dataclasses import dataclass

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
        self.ex = kwargs.get("xp")


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
