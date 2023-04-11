"""
This module contains utility functions for calculating
the glory of a player and getting the elo reset.
"""

from math import floor, log10


def get_glory_from_wins(total_wins: int) -> int:
    """
    Calculates the glory of a player based on their total wins.

    :param total_wins: The total wins of the player.
    :return: The calculated glory of the player.

    """
    if total_wins <= 150:
        return 20 * total_wins
    return floor((10 * (45 * (log10(total_wins * 2) ** 2))) + 245)


def get_glory_from_best_rating(best_rating: int) -> int:
    """
    Calculates the glory of a player based on their best rating.

    :param best_rating: The best rating of the player.
    :return: The calculated glory of the player.

    """
    retval = 0
    if best_rating < 1200:
        retval = 250
    elif 1200 <= best_rating < 1286:
        retval = 10 * (25 + (0.872093023 * (86 - (1286 - best_rating))))
    elif 1286 <= best_rating < 1390:
        retval = 10 * (100 + (0.721153846 * (104 - (1390 - best_rating))))
    elif 1390 <= best_rating < 1680:
        retval = 10 * (187 + (0.389655172 * (290 - (1680 - best_rating))))
    elif 1680 <= best_rating < 2000:
        retval = 10 * (300 + (0.428125 * (320 - (2000 - best_rating))))
    elif 2000 <= best_rating < 2300:
        retval = 10 * (437 + (0.143333333 * (300 - (2300 - best_rating))))
    elif best_rating >= 2300:
        retval = 10 * (480 + (0.05 * (400 - (2700 - best_rating))))
    return floor(retval)


def get_hero_elo_from_old_elo(old_elo: int) -> int:
    """
    Calculates the hero Elo rating of a player based on their previous Elo rating.

    :param old_elo: The previous Elo rating of the player.
    :return: The hero Elo rating of the player after the calculation.

    """
    if old_elo < 2000:
        return floor((old_elo + 375) / 1.5)
    return floor(1583 + (old_elo - 2000) / 10)


def get_personal_elo_from_old_elo(old_elo: int) -> int:
    """
    Calculates the personal Elo rating of a player based on their previous Elo rating.

    :param old_elo: The previous Elo rating of the player.
    :return: The personal Elo rating of the player after the calculation.
    """
    if old_elo >= 1400:
        return floor(1400 + (old_elo - 1400.0) / (3.0 - (3000 - old_elo) / 800.0))
    return old_elo
