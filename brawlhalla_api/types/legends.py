"""
This module provides two dataclass, Legend and LegendDetails.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass, field

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla


@dataclass
class Legend:
    """
    Legend represents a Brawlhalla Legend and contains basic information.

    brawlhalla: an instance of the Brawlhalla class
    legend_id: the legend's unique ID
    legend_name_key: the legend's name key
    bio_name: the legend's bio name
    bio_aka: the legend's bio aka
    weapon_one: the legend's first weapon
    weapon_two: the legend's second weapon
    strength: the legend's strength
    dexterity: the legend's dexterity
    defense: the legend's defense
    speed: the legend's speed

    """

    brawlhalla: Brawlhalla = field(repr=False)
    legend_id: int
    legend_name_key: str
    bio_name: str
    bio_aka: str
    weapon_one: str
    weapon_two: str
    strength: int
    dexterity: int
    defense: int
    speed: int

    def __init__(
        self,
        brawlhalla: Brawlhalla,
        **kwargs,
    ) -> None:
        self.brawlhalla = brawlhalla
        self.__dict__.update(kwargs)
        self.strength = int(self.strength)
        self.dexterity = int(self.dexterity)
        self.defense = int(self.defense)
        self.speed = int(self.speed)


@dataclass
class LegendDetails(Legend):
    """

    LegendDetails is a subclass of Legend and contains additional information.

    bio_quote: the legend's quote
    bio_quote_about_attrib: the legend's quote about attrib
    bio_quote_from: the legend's quote from
    bio_quote_from_attrib: the legend's quote from attrib
    bio_text: the legend's quote
    bot_name: the legend's bot name

    """

    bio_quote: str
    bio_quote_about_attrib: str
    bio_quote_from: str
    bio_quote_from_attrib: str
    bio_text: str
    bot_name: str

    def __init__(
        self,
        brawlhalla: Brawlhalla,
        **kwargs,
    ) -> None:
        super().__init__(brawlhalla, **kwargs)
        self.__dict__.update(kwargs)
