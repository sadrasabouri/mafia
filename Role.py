from dataclasses import dataclass, field
from mimetypes import init
from typing import List
import mafia_params
import lang
import enum

@dataclass
class Team:
    name : str
    
    def __repr__(self) -> str:
        return self.name.capitalize()

@dataclass(frozen= True)
class Role:
    name : str
    team : Team
    repitition : int

    def get_name(self, is_farsi : bool = False) -> str:
        if is_farsi:
            return lang.persian.get_name(self.name)
        return self.name

    def get_description(self, is_farsi : bool = False) -> str:
        if is_farsi:
            return lang.persian.get_description(self.name)
        return lang.english.get_description(self.name)

    def is_mafia(self) -> bool:
        return self.team == MAFIA

    def __hash__(self):
        return hash(self.name)

# Teams initiation
MAFIA = Team("mafia")
CITY = Team("city")
SERIAL_KILLER = Team("serial_killer")

#Roles initiation

@dataclass
class RoleFactory:
    name : str

    def get_team(self) -> str:
        return Team(mafia_params.role2team[self.name])

    def get_repitition(self) -> int:
        return int(mafia_params.nRoles[self.name])

    # get desription(self) -> str here

    def build(self) -> str:
        return Role(
            name = self.name,
            team = self.get_team(),
            repitition = self.get_repitition()
        )

class Roles(enum.Enum):
    #could've used enum.auto()
    BOXER = 0
    BRIDE = 1
    BULLETPROOF = 2
    BUS_DRIVER = 3
    CHEF = 4
    CLOWN = 5
    CURIOUS_KID = 6
    DETECTIVE = 7
    DOCTOR = 8
    DON = 9
    GENIE = 10
    GRANDMA = 11
    GROOM = 12
    HIT_MAN = 13
    INSANE = 14
    JAILER = 15
    JUDGE = 16
    KIND_WIFE = 17
    LAWYER = 18
    MADE_MAN = 19
    MAFIA = 20
    MAGICIAN = 21
    MILLER = 22
    POSTMAN = 23
    PRIEST = 24
    REBEL = 25
    REPORTER = 26 
    RESIDENT = 27
    SERIAL_KILLER = 28
    STUDENT = 29
    UNDERCOVER_COP = 30

    def get_name(self) -> str:
        return " ".join([word.capitalize() for word in self.name.split("_")])

    def to_role(self) -> Role:
        return RoleFactory(self.get_name()).build()

def get(string : str) -> Roles:
    return Roles["_".join([word.upper() for word in string.split()])]

roles = dict([(r, r.to_role()) for r in Roles])
ordered_roles = [roles.get(get(key)) for key in mafia_params.ordered_roles]