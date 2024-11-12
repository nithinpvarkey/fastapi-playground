from fastapi import FastAPI, HTTPException
from typing import Dict, List 
from schemas import GeneralURLChoices,Players

app = FastAPI()

PLAYERS = [
    {"id":1, "name":"Messi", "team": "Argentina"},
    {"id":2, "name":"Iniesta", "team": "Spain"},
    {"id":3, "name":"Ronaldo", "team": "Brazil"},
    {"id":4, "name":"Rooney", "team": "England"},
]

@app.get("/players")
async def palyers_list() -> List[Players]:
    return [
        Players(**P) for P in PLAYERS
    ]


@app.get("/players/{team_id}")
async def team_player(team_id: int ) -> Players:
    team = next((Players(**t) for t in PLAYERS if t['id']== team_id), None)

    #    # If no player with the specified team ID is found, raise a 404 error
    if team is None:
        raise HTTPException(status_code = 404, detail ="team not found")
        
    return team