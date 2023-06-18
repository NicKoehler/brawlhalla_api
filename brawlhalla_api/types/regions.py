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
        region = {
            2: Region.US_E,
            3: Region.EU,
            4: Region.SEA,
            5: Region.BRZ,
            6: Region.AUS,
            7: Region.US_W,
            8: Region.JPN,
            9: Region.SA,
            10: Region.ME,
        }.get(region_id)

        if region is None:
            raise ValueError(f"Unknown region id: {region_id}")

        return region

    def __str__(self) -> str:
        return self.value.upper()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__str__()})"
