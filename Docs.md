# Endpoints

---
```sh
POST /api/v2/uuid_from_username
```
Arguments: `username=(name)`

gets uuid from the mojang api and queues the player for hypixel api

### Response
*on success*
```json
{
    "status": "success",
    "uuid": uuid
}
```
*on failure*
```json
{
    "status": "error",
    "error": "error message"
}
```
---

```sh
POST /api/v2/stats/get
```
Arguments: `username=(name)`

If available, return stats of a player, otherwise add it to the queue from the hypixel api

If you need to collect many players please use the get_many endpoint as it groups the requests to the mojang api, saving api calls

this request will add the player that is requested to the queue to be polled for stats, if the stats are already cached it will return them. by default the stats will be cached for 7 days, this can be changed by modifying main.py

### Response
*on success*
```json
{
    "status": "success"
}
```
OR
```json
{
    "status": "success",
    "Username": {
        "uuid": uuid,
        "wins": WinCount,
        "losses": LossCount,
        ...
    }

}
```
*on failure*
```json
{
    "status": "error",
    "error": "error message"
}
```

---

```sh
POST /api/v2/stats/get_many
```

Arguments: `usernames= [name1, name2, ...]`

Similar to `/api/v2/stats/get` but allows for multiple players to be requested at once.


### Response
*on success*
```json
{
    "status": "success"
}
```
OR
```json
{
    "status": "success",
    "Username1": {
        "uuid": uuid,
        "wins": WinCount,
        "losses": LossCount,
        ...
    },

    "Username2": { ... },

    ...

}
```
*on failure*
```json
{
    "status": "error",
    "error": "error message"
}
```

---
```sh
GET /api/v2/cosmetics/capes?user=[name]
```
Not Implemented

---
```sh
GET /api/v2/cosmetics/ears?user=[name]
```
Not Implemented

---
```sh
GET /api/v2/cosmetics/wings?user=[name]
```
Not Implemented

---