"""
This module provides two dataclass, Legend and LegendDetails.

Both classes take a Brawlhalla instance as a parameter
and can be instantiated with optional keyword arguments that
correspond to the legend's attributes. If an attribute is not provided,
it defaults to None.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass

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

    def __init__(
        self,
        brawlhalla: Brawlhalla,
        **kwargs,
    ) -> None:
        self.brawlhalla = brawlhalla
        self.legend_id = kwargs.get("legend_id")
        self.legend_name_key = kwargs.get("legend_name_key")
        self.bio_name = kwargs.get("bio_name")
        self.bio_aka = kwargs.get("bio_aka")
        self.weapon_one = kwargs.get("weapon_one")
        self.weapon_two = kwargs.get("weapon_two")
        self.strength = int(kwargs.get("strength"))
        self.dexterity = int(kwargs.get("dexterity"))
        self.defense = int(kwargs.get("defense"))
        self.speed = int(kwargs.get("speed"))


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

    def __init__(
        self,
        brawlhalla: Brawlhalla,
        **kwargs,
    ) -> None:
        super().__init__(brawlhalla, **kwargs)
        self.bio_quote = kwargs.get("bio_quote")
        self.bio_quote_about_attrib = kwargs.get("bio_quote_about_attrib")
        self.bio_quote_from = kwargs.get("bio_quote_from")
        self.bio_quote_from_attrib = kwargs.get("bio_quote_from_attrib")
        self.bio_text = kwargs.get("bio_text")
        self.bot_name = kwargs.get("bot_name")
