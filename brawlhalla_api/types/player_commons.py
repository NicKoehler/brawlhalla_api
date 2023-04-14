"""
This module defines PlayerCommons class,
which contains commons information about a player in the game Brawlhalla.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla


@dataclass
class PlayerCommons:
    """
    PlayerCommons never gets instantiated directly.
    Instead it gets instantiated by PlayerRanked
    and PlayerRankedLegend as they share some common properties
    """

    def __init__(self, brawlhalla: Brawlhalla, **kwargs) -> None:
        self.brawlhalla = brawlhalla
        self.__dict__.update(kwargs)
