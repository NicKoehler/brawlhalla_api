from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses import dataclass

from .player_clan import PlayerClan
from .player_legend import PlayerStatsLegend

if TYPE_CHECKING:
    from brawlhalla_api import Brawlhalla
    from brawlhalla_api.types import Clan


@dataclass
class PlayerStats:
    def __init__(
        self,
        brawlhalla: Brawlhalla,
        **kwargs,
    ) -> None:
        self.brawlhalla = brawlhalla
        self.brawlhalla_id = kwargs.get("brawlhalla_id")
        self.name = kwargs.get("name").encode("raw_unicode_escape").decode("utf-8")
        self.xp = kwargs.get("xp")
        self.level = kwargs.get("level")
        self.xp_percentage = kwargs.get("xp_percentage")
        self.games = kwargs.get("games")
        self.wins = kwargs.get("wins")
        self.damagebomb = int(kwargs.get("damagebomb"))
        self.damagemine = int(kwargs.get("damagemine"))
        self.damagespikeball = int(kwargs.get("damagespikeball"))
        self.damagesidekick = int(kwargs.get("damagesidekick"))
        self.hitsnowball = kwargs.get("hitsnowball")
        self.kobomb = kwargs.get("kobomb")
        self.komine = kwargs.get("komine")
        self.kospikeball = kwargs.get("kospikeball")
        self.kosidekick = kwargs.get("kosidekick")
        self.kosnowball = kwargs.get("kosnowball")
        self.legends = [
            PlayerStatsLegend(brawlhalla, **legend) for legend in kwargs.get("legends")
        ]
        self.clan = (
            PlayerClan(brawlhalla, **kwargs.get("clan")) if "clan" in kwargs else None
        )

    async def get_clan(self) -> Clan | None:
        """
        Gets the clan of the player.

        :return: An object of type `Clan`,
            containing the player's clan or `None` if the player is not in a clan.
        """
        if self.clan is None:
            return

        return await self.brawlhalla.get_clan(self.clan.clan_id)
