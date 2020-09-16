from dataclasses import dataclass, field
from mimetypes import init
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

#Roles initiation
class Roles(enum.Enum):
    BOXER = Role("Boxer", MAFIA)
    BRIDE = Role("Bride", CITY)
    BULLETPROOF = Role("Bulletproof", CITY)
    BUS_DRIVER = Role("Bus Driver", CITY)
    CHEF = Role("Chef", CITY)
    CLOWN = Role("Clown", CITY)
    CURIOUS_KID = Role("Curious Kid", CITY)
    DETECTIVE = Role("Detective", CITY)
    DOCTOR = Role("Doctor" , CITY)
    DON = Role("Don", MAFIA)
    GENIE = Role("Genie", CITY)
    GRANDMA = Role("Grandma", CITY)
    GROOM = Role("Groom", CITY)
    HIT_MAN = Role("Hit Man", MAFIA)
    INSANE = Role("Insane", CITY)
    JAILER = Role("Jailer", CITY)
    JUDGE = Role("Judge", CITY)
    KIND_WIFE = Role("Kind Wife", MAFIA)
    LAWYER = Role("Lawyer", MAFIA)
    MADE_MAN = Role("Made Man", MAFIA)
    MAFIA = Role("Mafia", MAFIA)
    MAGICIAN = Role("Magician", CITY)
    MILLER = Role("Miller", CITY)
    POSTMAN = Role("Postman", CITY)
    PRIEST = Role("Priest", CITY)
    REBEL = Role("Rebel", CITY)
    REPORTER = Role("Reporter", CITY)
    RESIDENT = Role("Resident" , CITY)
    SERIAL_KILLER = Role("Serial Killer", SERIAL_KILLER)
    STUDENT = Role("Student", CITY)
    UNDER_COVER_COP = Role("Undercover Cop", CITY)