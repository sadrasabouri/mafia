from sys import argv
from random import randrange, shuffle
from typing import Callable, Dict, List, Text, Tuple
from flask import Flask, render_template, url_for, request
from flask_httpauth import HTTPBasicAuth
from mafia_params import max_comments, role2team
from player import Player
from Role import Role, Roles, roles, ordered_roles

is_farsi_mode : bool = True

class PlayerManager:
    n_players : int
    roles : List[Role]
    
    ip2player : Dict[str, str] = {}
    player_id : int = 0
    n_comments = 0
    comments_ordered = []

    def __init__(self, n_players : int, roles : List[Role]):
        self.n_players = n_players
        self.roles = roles

    def is_ip_valid(self, ip : str) -> bool:
        return ip in self.ip2player.keys()

    def get_player(self, ip : str):
        if not self.is_ip_valid(ip):
            return None
        return self.ip2player[ip]

    def get_next_role(self) -> Role:
        return self.roles[self.player_id]

    def new_player(self, ip : str, username : str) -> Player:
        if self.player_id > self.n_players:
            return None 
        role = self.get_next_role()
        image_name = role.get_name() + "_" + str(randrange(1, role.repitition + 1))
        player = Player(ip, username, role.get_name(), image_name)
        self.ip2player[ip] = player
        
        self.player_id += 1

        # log new player
        print("*" * 20, "New Player","*" * 20)
        to_god = ip + " : " + str(self.player_id) + " : " + username +  " --> " + role.get_name()
        if is_farsi_mode:
            to_god += "/" + role.get_name(is_farsi= True)
        print(to_god)

        return player

    def comment(self, player : Player):
        player.set_comment(True)
        self.n_comments += 1
        self.comments_ordered.append(player.get_ip())
    
    def uncomment(self, player : Player):
        player.set_comment(False)
        self.n_comments -= 1
        self.comments_ordered.remove(player.get_ip())        

app = Flask(__name__)
auth = HTTPBasicAuth()
auth_GOD = HTTPBasicAuth()
preshared_key : str = ""

player_manager = None

@auth.verify_password
def verify_password(username, password):
    if len(username) > 0:
        return username

@app.route('/')
@auth.login_required
def index():
    username = str(auth.current_user())
    ip = str(request.remote_addr)

    # redirect current players
    if player_manager.is_ip_valid(ip):
        return render_template("Player.html", player=player_manager.get_player(ip))

    # create new player
    role = player_manager.get_next_role()
    player : Player = player_manager.new_player(ip, username)
    
    # reject excess players
    if player is None:
        return not_found_page()

    return render_template("index.html",
                            image_name=player.image_name,
                            role_name=role.name, role_name_fa=role.get_name(is_farsi= True),
                            description=role.get_description(), description_fa=role.get_description(is_farsi= True),
                            is_farsi=True)

@auth_GOD.verify_password
def verify_password_god(username, password):
    if password == preshared_key:
        return username

@app.route('/GOD')
@auth_GOD.login_required
def god_page():
    def kill(player : Player) -> None:
        # notice banned players cannot be killed
        if player.is_alive():
            player.die()

    def switch_ban(player : Player) -> None:
        player.switch_ban()

    def comment(player : Player) -> None:
        if player.get_comment() is False:
            if player_manager.n_comments > max_comments(nPlayers):
                nonlocal msg
                msg = "Error: Out of Comments."
                return
            player_manager.comment(player)
        else:
            player_manager.uncomment(player)

    request_mapper : Dict[str, Callable] = {
        "Kill": kill,
        "Ban": switch_ban,
        "Comment": comment
    }

    # filters out invalid requests
    def get_requests() -> List[Tuple[str, Player]]:
        requests = []
        for key in request_mapper.keys():
            ip = request.args.get(key)
            
            if ip is None:
                continue
            if not player_manager.is_ip_valid(ip):
                print("invalid ip / request: ", ip, f"({key})")
                return -1

            player = player_manager.get_player(ip)
            requests.append((key, player))
        return requests

    msg = ""

    request_list = get_requests()
    if request_list == -1:
        return not_found_page()

    # handle requests
    for req, player in request_list:
        request_mapper[req](player)
    
    return render_template("GOD.html", ip2player=player_manager.ip2player,
                           prompt_message=msg, roles={role.get_name() : roles.count(role) for role in set(roles)},
                           comments=player_manager.comments_ordered, role2team=role2team)

@app.errorhandler(404) 
def invalid_route(e):
    return not_found_page()

def not_found_page() -> Text:
    return render_template("404.html", is_farsi=True)

def help_me():
    usage = "-" * 70 + "\n"
    usage += "mafia - Web Server Application For Mafia Game Playing On Local Network \n\n"
    usage += "-" * 70 + "\n"
    usage += "Usage: python3 mafia number_of_players[int]\n"
    usage += "ex: python3 mafia 5\n"
    usage += "this will tell mafia.py that you want a game for 5 people.\n\n"
    usage += "If you've seen a bug here (or any idea that can help us) feel free to open an issue\n"
    usage += "here at : https://github.com/sadrasabouri/mafia/issues"
    print(usage)
    exit()

def give_me_roles(ordered_roles):
    """
    Check the number of players and roles.

    :param ordered_roles: ordered roles
    :type ordered_roles: list
    :return: a valid list for roles
    """
    n = len(ordered_roles)
    if n >= 14:
        ordered_roles[12] = Roles.GROOM
        ordered_roles[13] = Roles.BRIDE
        if n % 3 == 0:
            ordered_roles[14] = Roles.SERIAL_KILLER
    if n % 3 != 0:
        try:
            i = ordered_roles.index(Roles.MAFIA)
            ordered_roles[i] = Roles.MADE_MAN
            ordered_roles[2] = Roles.REPORTER
        except ValueError:
            pass
    if n % 3 == 2:
        try:
            i = ordered_roles.index(Roles.MAFIA)
            ordered_roles[i] = Roles.KIND_WIFE
        except ValueError:
            pass
    return ordered_roles

def gen_preshared_key() -> str:
    key = ""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    for _ in range(4):
        key += chars[randrange(0, len(chars))]
    return key

if __name__ == "__main__":
    # parse args
    if len(argv) < 2 or argv[1] in ['--help', 'help', '-h']:
        help_me()
    nPlayers = int(argv[1])

    # make roles
    if nPlayers > len(ordered_roles):
        print("Too many players, mafia doesn't support a game with", nPlayers, "player.")
        help_me()
    roles = give_me_roles(ordered_roles[:nPlayers])
    shuffle(roles)
    
    player_manager = PlayerManager(n_players= nPlayers, roles= roles)

    # preshared key generation
    preshared_key = gen_preshared_key()
    print("_" * 20 + "GOD's password" + "_" * 20)
    print(preshared_key)
    print("_" * 54)

    app.run(host="0.0.0.0",
            port=5000,
            use_reloader=False)