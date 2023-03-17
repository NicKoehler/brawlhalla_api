# <img src="https://cdn2.steamgriddb.com/file/sgdb-cdn/icon/dd50e4d9c47cdf72d24e89d248edb35b/32/256x256.png"  height="25"> · Brawlhalla API

_An unofficial brawlhalla api implementation_

## Table of contents

- [Introduction](#introduction)

- [Installation](#installation)
- [Usage](#usage)

  - [Authentication](#authentication)
  - [Examples](#examples)
    - [Asyncio](#asyncio)
    - [Without asyncio](#without-asyncio)

- [License](#license)

- [Contributions](#contributions)

## Introduction

This library provides an easy-to-use interface to interact with the Brawlhalla API. Users can retrieve information such as player rankings, player statistics, and more. The library also supports asynchronous requests, making it efficient to handle multiple requests simultaneously.

## Installation

To install the Brawlhalla API library, use pip:

```bash
pip install git+https://github.com/nickoehler/brawlhalla_api
```

## Usage

### Authentication

To use the Brawlhalla API, you need to provide an API key.
Send an email to api@brawlhalla.com with a detailed description of how you intend to use the service.

### Examples

#### Asyncio

```python
import asyncio
from brawlhalla_api import Brawlhalla

API_KEY = "..." # use your api key

async def main():
    brawl = Brawlhalla(API_KEY)
    players = await brawl.get_rankings()

    # printing every player
    for player in players:
        print(player.name)

    # get stats of the first player
    stats = await players[0].get_stats()
    ranked = await players[0].get_ranked()

asyncio.run(main())
```

#### Without asyncio

```python
from brawlhalla_api import BrawlhallaSync

API_KEY = "..." # use your api key

brawl = BrawlhallaSync(API_KEY)
players = brawl.get_rankings()

# printing every player
for player in players:
    print(player.name)

# get stats of the first player
stats = players[0].get_stats()
ranked = players[0].get_ranked()
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributions

Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes and commit them with clear commit messages
4. Push your changes to your forked repository
5. Submit a pull request

> Before making any significant changes, please open an issue to discuss the changes you plan to make.
