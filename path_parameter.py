from fastapi import FastAPI, HTTPException
from typing import Dict, List # list[dict] syntax for type hints is only supported in Python 3.9 and later
                              # For earlier versions, you should use List and Dict from the typing module.
from enum import Enum

class GeneralURLChoices(Enum):
    MESSI = "messi"
    INIESTA ="iniesta"
    RONALDO = "ronaldo"
    ROONEY = "rooney"



app = FastAPI()

players = [
    {"id":1, "name":"Messi", "team": "Argentina"},
    {"id":2, "name":"Iniesta", "team": "Spain"},
    {"id":3, "name":"Ronaldo", "team": "Brazil"},
    {"id":4, "name":"Rooney", "team": "England"},
]

## Define an asynchronous GET endpoint to retrieve the list of all players
@app.get("/players")
async def palyers_list() -> List[Dict]:
    return players

## Define an asynchronous GET endpoint to retrieve a specific player by their team ID - (PATH PARAMETER)
@app.get("/players/{team_id}")
async def team_player(team_id: int ) -> Dict:
    team = next((t for t in players if t['id']== team_id), None)

    #    # If no player with the specified team ID is found, raise a 404 error
    if team is None:
        raise HTTPException(status_code = 404, detail ="team not found")
        
    return team

# Define an Enum to represent player names as URL path choices
@app.get("/players/team/{player}")
async def player_team(player: GeneralURLChoices) -> List[Dict]:
    return [
        p for p in players if p["name"].lower() == player.value
    ]