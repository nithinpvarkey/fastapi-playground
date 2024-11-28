from fastapi import FastAPI, HTTPException
from typing import Dict, List # list[dict] syntax for type hints is only supported in Python 3.9 and later
                              # For earlier versions, you should use List and Dict from the typing module.

from POST_schemas import GeneralURLChoices,Players,Create_players,Players_with_id

app = FastAPI()

PLAYERS = [
    {"id":1, "name":"Messi", "team": "Argentina"},
    {"id":2, "name":"Iniesta", "team": "Spain"},
    {"id":3, "name":"Ronaldo", "team": "Brazil"},
    {"id":4, "name":"Rooney", "team": "England"},
]
# GET endpoint to retrieve the list of players
@app.get("/players")
async def palyers_list() -> List[Players]:
    return [
        Players(**P) for P in PLAYERS
    ]

# POST endpoint to add a new player to the list
@app.post("/players")
async def create_player(player_data: Create_players) -> Players_with_id:
    id = PLAYERS[-1]["id"]+1   # Generate a new unique ID based on the last player's ID
    player = Players_with_id(id=id, **player_data.model_dump()).model_dump()  # Create a new player with the provided data and the generated ID
    PLAYERS.append(player)
    return player