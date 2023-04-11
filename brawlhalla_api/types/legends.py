"""
This module provides two dataclass, Legend and LegendDetails.
Legend represents a Brawlhalla Legend and contains basic information such as:
name, weapons, stats etc.

LegendDetails is a subclass of Legend and contains additional information such as
the legend's bio, quotes etc.

Both classes take a Brawlhalla instance as a parameter
and can be instantiated with optional keyword arguments that
correspond to the legend's attributes. If an attribute is not provided,
it defaults to None.

Note: These classes require the brawlhalla_api module to be imported,
otherwise a NameError will be raised.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla


@dataclass
class Legend:
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
