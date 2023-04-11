"""
This module contains the PlayerClan class,
which represents a player's clan in the game Brawlhalla.

"""


from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses import dataclass

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla


@dataclass
class PlayerClan:
    """
    A class representing a player's clan in the Brawlhalla game.
    :param brawlhalla: An instance of the `Brawlhalla` class representing the game.
    """

    def __init__(
        self,
        brawlhalla: Brawlhalla,
        **kwargs,
    ) -> None:
        self.brawlhalla = brawlhalla
        self.clan_name = (
            kwargs.get("clan_name").encode("raw_unicode_escape").decode("utf-8")
        )
        self.clan_id = kwargs.get("clan_id")
        self.clan_xp = int(kwargs.get("clan_xp"))
        self.personal_xp = kwargs.get("personal_xp")
