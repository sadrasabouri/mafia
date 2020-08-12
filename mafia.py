from sys import argv
from random import randrange, shuffle
from flask import Flask, render_template, url_for, request
from flask_httpauth import HTTPBasicAuth
from mafia_params import *

app = Flask(__name__)
auth = HTTPBasicAuth()
id = 0
nPlayers = 0
roles = []
ip2role_idx = {}

@auth.verify_password
def verify_password(username, password):
    if len(username) > 0:
        return username
    return None

@app.route('/')
@auth.login_required
def index():
    global id, ip2role_idx
    role = ""
    image_name = ""
    ip = str(request.remote_addr)

    if ip in ip2role_idx.keys():
        role = ip2role_idx[ip][0]
        image_name = ip2role_idx[ip][0] + "_" + str(ip2role_idx[ip][1])
    else:
        if id > nPlayers:
            return "Numbers of players out of range!"   #TODO:well defined Error Page
        role = roles[id]
        ip2role_idx[ip] = (role, str(randrange(1, nRoles[role] + 1)))
        image_name = role + "_" + str(ip2role_idx[ip][1])
        print("*" * 20, "New Player","*" * 20)
        print(ip + " : " + str(id) + " --> " + role)
        id += 1
    return render_template("index.html",
                            image_name=image_name,
                            role_name=role, role_name_fa=role2fa[role],
                            description=descriptions[role], description_fa=descriptions_fa[role],
                            player_id=id - 1,
                            is_farsi=True)


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


if __name__ == "__main__":
    if len(argv) < 2 or argv[1] in ['--help', 'help', '-h']:
        help_me()
    nPlayers = int(argv[1])
    if nPlayers > len(ordered_roles):
        print("Too many players, mafia doesn't support a game with", nPlayers, "player.")
        help_me()
    roles = ordered_roles[:nPlayers]
    shuffle(roles)
    app.run(host="0.0.0.0", \
            port=5000, \
            debug=True)
