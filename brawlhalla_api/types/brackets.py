"""
This module defines Bracket data class which represents
a bracket in the game Brawlhalla.
"""

from enum import Enum


class Bracket(Enum):
    """
    Bracket represents a bracket in the game Brawlhalla.
    """

    SINGLE = "1v1"
    DOUBLE = "2v2"
    ROTATING = "rotating"
