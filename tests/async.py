import pytest
from os import environ
from time import sleep
from dotenv import load_dotenv

from brawlhalla_api import Brawlhalla
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
    return Brawlhalla(API_KEY)


@pytest.fixture(autouse=True)
def slow_down_tests():
    sleep(0.5)


@pytest.mark.asyncio
async def test_search(brawl: Brawlhalla):
    result = await brawl.search(76561198025185087)
    assert isinstance(result, SteamUser)


@pytest.mark.asyncio
async def test_rankings(brawl: Brawlhalla):
    result = await brawl.get_rankings()
    assert isinstance(result[0], RankingResult)


@pytest.mark.asyncio
async def test_rankings_with_name(brawl: Brawlhalla):
    result = await brawl.get_rankings(name="Nickoehler")
    assert len(result) == 0


@pytest.mark.asyncio
async def test_stats(brawl: Brawlhalla):
    result = await brawl.get_stats(3358533)
    assert isinstance(result, PlayerStats)


@pytest.mark.asyncio
async def test_ranked(brawl: Brawlhalla):
    result = await brawl.get_ranked(3358533)
    assert isinstance(result, PlayerRanked)


@pytest.mark.asyncio
async def test_clan(brawl: Brawlhalla):
    result = await brawl.get_clan(1754020)
    assert isinstance(result, Clan)


@pytest.mark.asyncio
async def test_legends(brawl: Brawlhalla):
    result = await brawl.get_legends()
    assert isinstance(result, list)


@pytest.mark.asyncio
async def test_specific_legend(brawl: Brawlhalla):
    result = await brawl.get_legends(3)
    assert isinstance(result, LegendDetails)


@pytest.mark.asyncio
async def test_get_stats_on_ranking(brawl: Brawlhalla):
    result = await brawl.get_rankings()
    assert isinstance(await result[0].get_stats(), PlayerStats)


@pytest.mark.asyncio
async def test_get_clan_on_player_stats(brawl: Brawlhalla):
    result = await (await brawl.get_stats(3358533)).get_clan()
    assert isinstance(result, Clan)


@pytest.mark.asyncio
async def test_errors(brawl: Brawlhalla):
    with pytest.raises(BadRequest):
        await brawl.get_rankings(bracket=Region.ALL)
