from sys import argv
from random import randrange, shuffle
from typing import Callable, Dict, List, Text, Tuple
from flask import Flask, render_template, url_for, request
from flask_httpauth import HTTPBasicAuth
from mafia_params import ordered_roles, nRoles, role2team, descriptions, descriptions_fa, role2fa, max_comments
from player import Player

app = Flask(__name__)
auth = HTTPBasicAuth()
auth_GOD = HTTPBasicAuth()
preshared_key = ""

ip2player = {}
roles = []
player_id = 0
nPlayers = 0

nComments = 0
comments_ordered = []

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
    if ip in ip2player.keys():
        return render_template("Player.html", player=ip2player[ip])

    # reject excess players
    global player_id
    if player_id > nPlayers:
        return not_found_page()

    # create new player
    role = roles[player_id]
    image_name = role + "_" + str(randrange(1, nRoles[role] + 1))
    ip2player[ip] = Player(ip, username, role, image_name)
    
    # next player id
    player_id += 1 
    
    # log new player
    print("*" * 20, "New Player","*" * 20)
    to_god = ip + " : " + str(player_id) + " : " + username +  " --> " + role
    to_god += "/" + role2fa[role]    #TODO: Just in Farsi Mode
    print(to_god)

    return render_template("index.html",
                            image_name=image_name,
                            role_name=role, role_name_fa=role2fa[role],
                            description=descriptions[role], description_fa=descriptions_fa[role],
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
        if nComments > max_comments(nPlayers):
            nonlocal msg
            msg = "Error: Out of Comments."
            return

        if player.get_comment() is False:
            global nComments, comments_ordered
            player.set_comment(True)
            nComments += 1
            comments_ordered.append(player.get_ip())
        else:
            player.set_comment(False)
            nComments -= 1
            comments_ordered.remove(player.get_ip())

    request_mapper : Dict[Callable] = {
        "Kill", kill,
        "Ban", switch_ban,
        "Comment", comment
    }

    # filters out invalid requests
    def get_requests() -> List[Tuple[str, Player]]:
        requests = []
        for key in request_mapper.keys():
            ip = request.args.get(key)

            if ip is None or ip not in ip2player.keys():
                print("invalid ip / request: ", ip, f"({key})")
                continue

            player = ip2player[ip]
            requests.append((key, player))

        return requests

    msg = ""

    request_list = get_requests()
    if len(request_list) == 0:
        return not_found_page()

    # handle requests
    for req, player in request_list:
        request_mapper[req](player)
    
    return render_template("GOD.html", ip2player=ip2player,
                           prompt_message=msg, roles={role:roles.count(role) for role in set(roles)},
                           comments=comments_ordered, role2team=role2team)

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
        ordered_roles[12] = 'Groom'
        ordered_roles[13] = 'Bride'
        if n % 3 == 0:
            ordered_roles[14] = 'Serial Killer'
    if n % 3 != 0:
        try:
            i = ordered_roles.index('Mafia')
            ordered_roles[i] = 'Made Man'
            ordered_roles[2] = 'Reporter'
        except ValueError:
            pass
    if n % 3 == 2:
        try:
            i = ordered_roles.index('Mafia')
            ordered_roles[i] = 'Kind Wife'
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
    
    # preshared key generation
    preshared_key = gen_preshared_key()
    print("_" * 20 + "GOD's password" + "_" * 20)
    print(preshared_key)
    print("_" * 54)

    app.run(host="0.0.0.0",
            port=5000,
            use_reloader=False)