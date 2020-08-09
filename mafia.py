from sys import argv
from random import randrange, shuffle
from flask import Flask, render_template, url_for, request
from mafia_params import *

app = Flask(__name__)
id = 0
nPlayers = 0
roles = []
ip2role = {}
ip2image = {}

@app.route('/')
def index():
    global id, ip2role, ip2image
    role = ""
    image_name = ""
    ip = str(request.remote_addr)

    if ip in ip2role.keys():
        role = ip2role[ip]
        image_name = ip2image[ip]
    else:
        if id > nPlayers:
            return "Numbers of players out of range!"   #TODO:well defined Error Page
        role = roles[id]
        image_name = role + "_" + str(randrange(1, nRoles[role] + 1))
        ip2role[ip] = role
        ip2image[ip] = image_name
        print("*" * 20, "New Player","*" * 20)
        print(ip + " : " + str(id) + " --> " + role)
        id += 1
    return render_template("index.html",
                            image_name=image_name,
                            role_name=role,
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
