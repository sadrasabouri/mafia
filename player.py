class Player:
    """A player in mafia game"""
    def __init__(self, ip, username, role, image_name):
        self.ip = ip
        self.username = username
        self.state = "alive"
        self.role = role
        self.image_name = image_name
        self.comment = False
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
        if state in ["alive", "dead", "banned"]:
            self.state = state
    def set_comment(self, comment):
        self.comment = comment 
    