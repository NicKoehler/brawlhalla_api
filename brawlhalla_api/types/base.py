from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from brawlhalla import Brawlhalla
    from brawlhalla_sync import BrawlhallaSync


class Base:
    def __init__(self, brawlhalla: Brawlhalla | BrawlhallaSync) -> None:
        self.brawlhalla = brawlhalla

    def __repr__(self):
        attrs = ", ".join(
            f"{k}: {v}" for k, v in vars(self).items() if k != "brawlhalla"
        )
        return f"{self.__class__.__name__}({attrs})"
