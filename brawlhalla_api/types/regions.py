from enum import Enum


class Region(Enum):
    EU = "eu"
    ALL = "all"
    SEA = "sea"
    BRZ = "brz"
    AUS = "aus"
    US_W = "us-w"
    US_E = "us-e"
    JPN = "jpn"

    def from_str(value: str) -> "Region":
        """
        This function is used to convert a region string to a Region enum.
        :param value: The region string to convert.
        :return: The region enum.
        """
        return Region(value.lower())

    def from_id(id: int) -> "Region":
        """
        This function is used to convert a region id to a Region enum.
        :param id: The region id to convert.
        :return: The region enum.
        """
        match id:
            case 1:
                return Region.JPN
            case 2:
                return Region.US_E
            case 3:
                return Region.EU
            case 4:
                return Region.SEA
            case 5:
                return Region.BRZ
            case 6:
                return Region.AUS
            case 7:
                return Region.US_W
            case _:
                raise ValueError(f"Unknown region id: {id}")

    def __str__(self) -> str:
        return self.value.upper()
