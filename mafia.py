from sys import argv
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",
                            image_name="Don",
                            role_name="Don",
                            is_farsi=True)


def help_me():
    usage  = "mafia - Web Server Application For Mafia Game Playing On Local Network \n\n"
    usage += "Usage: python3 mafia number_of_players[int]\n"
    usage += "ex: python3 mafia 5\n"
    usage += "this will tell mafia.py that you want a game for 5 people."
    print(usage)
    exit()


if __name__ == "__main__":
    if len(argv) < 2 or argv[1] in ['--help', 'help', '-h']:
        help_me()
    nPlayers = int(argv[1])
    app.run(host="0.0.0.0", \
            port=5000, \
            debug=True)
