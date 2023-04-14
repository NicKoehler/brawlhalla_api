"""
This module defines PlayerClan class,
which represents a player's clan in the game Brawlhalla.

"""


from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass, field

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla


@dataclass
class PlayerClan:
    """
    A class representing a player's clan in the Brawlhalla game.
    :param brawlhalla: An instance of the `Brawlhalla` class representing the game.
    """

    brawlhalla: Brawlhalla = field(repr=False)
    clan_name: str
    clan_id: int
    clan_xp: int
    personal_xp: int

    def __init__(
        self,
        brawlhalla: Brawlhalla,
        **kwargs,
    ) -> None:
        self.brawlhalla = brawlhalla
        self.__dict__.update(kwargs)
        self.clan_name = self.clan_name.encode("raw_unicode_escape").decode("utf-8")
        self.clan_xp = int(self.clan_xp)
