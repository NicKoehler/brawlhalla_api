from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla, BrawlhallaSync

from .base import Base


class Legend(Base):
    def __init__(
        self,
        brawlhalla: Brawlhalla | BrawlhallaSync,
        legend_id: int = None,
        legend_name_key: str = None,
        bio_name: str = None,
        bio_aka: str = None,
        weapon_one: str = None,
        weapon_two: str = None,
        strength: int = None,
        dexterity: int = None,
        defense: int = None,
        speed: int = None,
    ) -> None:
        self.legend_id = legend_id
        self.legend_name_key = legend_name_key
        self.bio_name = bio_name
        self.bio_aka = bio_aka
        self.weapon_one = weapon_one
        self.weapon_two = weapon_two
        self.strength = int(strength)
        self.dexterity = int(dexterity)
        self.defense = int(defense)
        self.speed = int(speed)
        super().__init__(brawlhalla)


class LegendDetails(Legend):
    def __init__(
        self,
        brawlhalla: Brawlhalla | BrawlhallaSync,
        legend_id: int = None,
        legend_name_key: str = None,
        bio_name: str = None,
        bio_aka: str = None,
        bio_quote: str = None,
        bio_quote_about_attrib: str = None,
        bio_quote_from: str = None,
        bio_quote_from_attrib: str = None,
        bio_text: str = None,
        bot_name: str = None,
        weapon_one: str = None,
        weapon_two: str = None,
        strength: int = None,
        dexterity: int = None,
        defense: int = None,
        speed: int = None,
    ) -> None:
        self.bio_quote = bio_quote
        self.bio_quote_about_attrib = bio_quote_about_attrib
        self.bio_quote_from = bio_quote_from
        self.bio_quote_from_attrib = bio_quote_from_attrib
        self.bio_text = bio_text
        self.bot_name = bot_name
        super().__init__(
            brawlhalla,
            legend_id,
            legend_name_key,
            bio_name,
            bio_aka,
            weapon_one,
            weapon_two,
            strength,
            dexterity,
            defense,
            speed,
        )
