# Fluorite Server
## _Fluorite Bot and Web Server Manager_

_No affiliation with Hypixel or Mojang_

Made in conjunction with [Fluorite Client](https://github.com/jh1236/Fluorite) (private repository)


Fluorite Server is an application focused around bedwars, being a  single app which manages the Fluorite Webserver and the Fluorite Bot, 
## Features
- Respects API ratelimits
- Caches data
- Automatically polls players for stats tracking (Event based triggers may be added in the future)
- Fetch player data endpoint for ingame stats
- Custom *Sweat Score* value to give aproximation of players skill level
- Cosmetics manager for [Fluorite Client](https://github.com/jh1236/Fluorite)
- Respects [Hypixel API Policies](https://developer.hypixel.net/policies/) as at 30/8/23

### Web Server Endpoints
please se Docs.md for more information
```sh
POST /api/v2/uuid_from_username
```
```sh
POST /api/v2/stats/get
```
```sh
POST /api/v2/stats/get_many
```
When able using the get_many endpoint is better as it uses less api calls to mojang
```sh
GET /api/v2/cosmetics/capes?user=[name]
```
```sh
GET /api/v2/cosmetics/ears?user=[name]
```
```sh
GET /api/v2/cosmetics/wings?user=[name]
```
---
### Discord Bot Commands
Currently work in progress, Discord bot not implimented yet
##### Admin commands
---
``Shutdown``

``Remove [player]``

``Remove_Dead``

``refactor``
##### User commands
---
``stats [plauyer]``

``uuid [username]``

``cosmetics [player]``

``capes [player]``

``top [statistic]``

``info``

## Installation & Setup
- Download and Install [Python](https://www.python.org/)
- Downlaod this repository
- Get [Hypixel API Key](https://developer.hypixel.net/dashboard)
- Get [Discord Bot Token](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications)
- Add Hypixel API key and Discord Bot Token to System Variables OR to .data/Tokens.json
- Install required libraries with `pip install -r requirements.txt`
- Update the data in data/bot.json with the channel id
- Run the program

*Please ensure your use of this api complies with [Hypixel API Policy](https://developer.hypixel.net/policies/), [Hypixel Terms of Service](https://hypixel.net/terms), [Mojang EULA](https://www.minecraft.net/en-us/eula), and [Discord Developer Policy](https://discord.com/developers/docs/policies-and-agreements/developer-policy)*