from dataclasses import dataclass
import mafia_params

@dataclass
class Team:
    name : str
    
    def __repr__(self) -> str:
        return self.name.capitalize()

@dataclass(frozen= True)
class Role:
    name : str
    team : Team

    def get_description(self, is_english : bool = True) -> str:
        if (is_english):
            return mafia_params.descriptions.get(self.name)
        return mafia_params.descriptions_fa.get(self.name)

    def is_mafia(self) -> bool:
        return self.team == MAFIA

# Teams initiation
MAFIA = Team("mafia")
CITY = Team("city")

#Roles initiation
RESIDENT = Role("Resident", CITY)
MAFIA = Role("Mafia", MAFIA)
