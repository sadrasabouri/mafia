from sys import argv
from random import randrange, shuffle
from typing import Text
from flask import Flask, render_template, url_for, request
from flask_httpauth import HTTPBasicAuth
from mafia_params import ordered_roles, nRoles, role2team, descriptions, descriptions_fa, role2fa
from player import Player

app = Flask(__name__)
auth = HTTPBasicAuth()
auth_GOD = HTTPBasicAuth()
preshared_key = ""
player_id = 0
nPlayers = 0
roles = []
ip2player = {}
nComments = 0
comments_ordered = []

@auth.verify_password
def verify_password(username, password):
    if len(username) > 0:
        return username
    return None

@app.route('/')
@auth.login_required
def index():
    global player_id, ip2player
    username = str(auth.current_user())
    role = ""
    image_name = ""
    ip = str(request.remote_addr)

    if ip in ip2player.keys():
        return render_template("Player.html", player=ip2player[ip])
    else:
        if player_id > nPlayers:
            return not_found_page()
        role = roles[player_id]
        image_name = role + "_" + str(randrange(1, nRoles[role] + 1))
        ip2player[ip] = Player(ip, username, role, image_name)
        print("*" * 20, "New Player","*" * 20)
        toGod = ip + " : " + str(player_id) + " : " + username +  " --> " + role
        toGod += "/" + role2fa[role]    #TODO: Just in Farsi Mode
        print(toGod)
        player_id += 1
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
def GOD_PAGE():
    global ip2player, nComments, comments_ordered
    msg = ""
    if request.args.get("Kill") is not None:
        ip = request.args.get("Kill")
        if ip in ip2player.keys():
            if ip2player[ip].get_state() == "alive":
                ip2player[ip].set_state("dead")
            else:
                ip2player[ip].set_state("alive")
        else:
            return not_found_page()
    if request.args.get("Ban") is not None:
        ip = request.args.get("Ban")
        if ip in ip2player.keys():
            if ip2player[ip].get_state() == "alive":
                ip2player[ip].set_state("banned")
            elif ip2player[ip].get_state() == "banned":
                ip2player[ip].set_state("alive")
        else:
            return not_found_page()
    if request.args.get("Comment") is not None:
        ip = request.args.get("Comment")
        if ip in ip2player.keys():
            if ip2player[ip].get_comment() is False:
                if nComments <= nPlayers // 3:
                    ip2player[ip].set_comment(True)
                    nComments += 1
                    comments_ordered.append(ip)
                else:
                    msg = "Error: Out of Comments."
            else:
                ip2player[ip].set_comment(False)
                nComments -= 1
                comments_ordered.remove(ip)
        else:
            return not_found_page()
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


if __name__ == "__main__":
    if len(argv) < 2 or argv[1] in ['--help', 'help', '-h']:
        help_me()
    nPlayers = int(argv[1])
    if nPlayers > len(ordered_roles):
        print("Too many players, mafia doesn't support a game with", nPlayers, "player.")
        help_me()
    roles = give_me_roles(ordered_roles[:nPlayers])
    shuffle(roles)
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    for i in range(4):
        preshared_key += chars[randrange(0, len(chars))]
    print("_" * 20 + "GOD's password" + "_" * 20)
    print(preshared_key)
    print("_" * 54)
    app.run(host="0.0.0.0",
            port=5000,
            use_reloader=False)
