from enum import Enum
from pydantic import BaseModel


class GeneralURLChoices(Enum):
    MESSI = "messi"
    INIESTA ="iniesta"
    RONALDO = "ronaldo"
    ROONEY = "rooney"

class Players(BaseModel):
     #{"id":1, "name":"Messi", "team": "Argentina"}
     id: int
     name: str
     team: str