import pytest
from os import environ
from time import sleep
from dotenv import load_dotenv

from brawlhalla_api import BrawlhallaSync
from brawlhalla_api.types import (
    Clan,
    Region,
    SteamUser,
    BadRequest,
    PlayerStats,
    PlayerRanked,
    RankingResult,
    LegendDetails,
)

load_dotenv()

API_KEY = environ.get("API_KEY")
assert API_KEY != None


@pytest.fixture
def brawl():
    return BrawlhallaSync(API_KEY)


@pytest.fixture(autouse=True)
def slow_down_tests():
    sleep(0.5)


def test_search(brawl: BrawlhallaSync):
    result = brawl.search(76561198025185087)
    assert isinstance(result, SteamUser)


def test_rankings(brawl: BrawlhallaSync):
    result = brawl.get_rankings()
    assert isinstance(result[0], RankingResult)


def test_rankings_with_name(brawl: BrawlhallaSync):
    result = brawl.get_rankings(name="Nickoehler")
    assert len(result) == 0


def test_stats(brawl: BrawlhallaSync):
    result = brawl.get_stats(3358533)
    assert isinstance(result, PlayerStats)


def test_ranked(brawl: BrawlhallaSync):
    result = brawl.get_ranked(3358533)
    assert isinstance(result, PlayerRanked)


def test_clan(brawl: BrawlhallaSync):
    result = brawl.get_clan(1754020)
    assert isinstance(result, Clan)


def test_legends(brawl: BrawlhallaSync):
    result = brawl.get_legends()
    assert isinstance(result, list)


def test_specific_legend(brawl: BrawlhallaSync):
    result = brawl.get_legends(3)
    assert isinstance(result, LegendDetails)


def test_get_stats_on_ranking(brawl: BrawlhallaSync):
    result = brawl.get_rankings()
    assert isinstance(result[0].get_stats(), PlayerStats)


def test_get_clan_on_player_stats(brawl: BrawlhallaSync):
    result = brawl.get_stats(3358533).get_clan()
    assert isinstance(result, Clan)


def test_errors(brawl: BrawlhallaSync):
    with pytest.raises(BadRequest):
        brawl.get_rankings(bracket=Region.ALL)
