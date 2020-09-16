from dataclasses import dataclass
from typing import List

class PlayerState:
    ALIVE : str = "alive"
    DEAD: str = "dead"
    BANNED: str = "banned"
    all: List[str] = [ALIVE, DEAD, BANNED]

"""A player in mafia game"""
@dataclass
class Player:
    ip : str
    username : str
    role : str
    image_name : str
    state : PlayerState = PlayerState.ALIVE
    comment : bool = False

    def is_alive(self) -> bool:
        return self.state == PlayerState.ALIVE

    def die(self) -> None:
        self.state = PlayerState.DEAD

    def switch_ban(self):
        self.unban() if self.is_banned() else self.ban()

    def is_banned(self) -> bool:
        return self.state == PlayerState.BANNED

    def ban(self):
        self.state = PlayerState.BANNED
    
    def unban(self):
        self.state = PlayerState.ALIVE

    def get_state(self):
        return self.state

    def get_ip(self):
        return self.ip

    def get_username(self):
        return self.username
    
    def get_role(self):
        return self.role
    
    def get_image_name(self):
        return self.image_name
    
    def get_comment(self):
        return self.comment

    def set_state(self, state):
        if state in PlayerState.all:
            self.state = state

    def set_comment(self, comment):
        self.comment = comment 
    