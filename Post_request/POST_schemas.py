from enum import Enum
from pydantic import BaseModel


class GeneralURLChoices(Enum):
    MESSI = "messi"
    INIESTA ="iniesta"
    RONALDO = "ronaldo"
    ROONEY = "rooney"

# Pydantic model for player data (without ID)
class Players(BaseModel):
     #{"id":1, "name":"Messi", "team": "Argentina"}
     name: str
     team: str
# Pydantic model for player data (without ID)  
class Create_players(Players):
     pass 

# Pydantic model for player data with an ID field    
class Players_with_id(Players):
     id: int