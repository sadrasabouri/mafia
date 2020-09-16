from dataclasses import dataclass, field
from mimetypes import init
import mafia_params
import lang

@dataclass
class Team:
    name : str
    
    def __repr__(self) -> str:
        return self.name.capitalize()

def get_team(s : str) -> Team:
    return Team(mafia_params.role2team[s])

@dataclass(frozen= False)
class Role:
    name : str
    team : Team = field(default= None)

    def __post_init__(self):
        self.team = get_team(self.name)

    def get_name(self, is_farsi : bool = False):
        if is_farsi:
            return lang.persian.get_name(self.name)
        return self.name

    def get_description(self, is_farsi : bool = False) -> str:
        if is_farsi:
            return lang.persian.get_description(self.name)
        return lang.english.get_description(self.name)

    def is_mafia(self) -> bool:
        return self.team == MAFIA

# Teams initiation
MAFIA = Team("mafia")
CITY = Team("city")
SERIAL_KILLER = Team("serial_killer")
