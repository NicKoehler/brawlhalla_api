"""
This module defines Region enum which represents
a region in the game Brawlhalla.
"""

from enum import Enum


class Region(Enum):
    """
    Region represents a region in the game Brawlhalla.
    """

    EU = "eu"
    ALL = "all"
    SEA = "sea"
    BRZ = "brz"
    AUS = "aus"
    US_W = "us-w"
    US_E = "us-e"
    JPN = "jpn"
    ME = "me"
    SA = "sa"

    @staticmethod
    def from_str(value: str) -> "Region":
        """
        This function is used to convert a region string to a Region enum.
        :param value: The region string to convert.
        :return: The region enum.
        """
        return Region(value.lower())

    @staticmethod
    def from_id(region_id: int) -> "Region":
        """
        This function is used to convert a region id to a Region enum.
        :param id: The region id to convert.
        :return: The region enum.
        """
        region = None
        match region_id:
            case 1:
                region = Region.JPN
            case 2:
                region = Region.US_E
            case 3:
                region = Region.EU
            case 4:
                region = Region.SEA
            case 5:
                region = Region.BRZ
            case 6:
                region = Region.AUS
            case 7:
                region = Region.US_W
            case 8:
                region = Region.ME
            case 9:
                region = Region.SA
            case _:
                raise ValueError(f"Unknown region id: {region_id}")
        return region

    def __str__(self) -> str:
        return self.value.upper()
