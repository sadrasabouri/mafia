# mafia
:dollar: Web Server Application For Mafia Game Playing On Local Network

Playing mafia game made easy simply by having: 
+ a system to run <b>mafia</b> on it (We call it FekroBot)
+ a hotspot that can provide a local host for us (your WIFI modem or your mobile hotspot)

There you go, lets play some mafia :sunglasses:.

<img src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/doc/Pictures/mafia_game.png">

## Usage
After cloning into mafia using command bellow:
```
$ git clone https://github.com/sadrasabouri/mafia
```
You should do these tiny steps:

0. <b>[Install pip3]</b>

First check if you have `pip3` installed in your system:
```
$ pip3 --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```
if you already have installed `pip3` you should see something like above, otherwise run the command bellow to install it:
```
$ sudo apt install python3-pip
```
1. <b>Instaling requiremets:</b>

Then install mafia requirements by
```
$ pip3 install -r requirements.txt
```
2. <b>Run the server application</b>

Now everything is ready, lets play:
run the command `$python3 mafia.py number_of_players[int]`, for example imagine you want to play mafia with 5 players.
```
$ python3 mafia.py 5
```
3. <b>Getting roles</b>

There you go, now each player can open a browser and type `serverhost:port_name`.

In defualt mode your address should be `server_ip:5000`.
| What player should see in the browser |
|:-------------------------------------:|
| <img width="324" height="576" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/doc/Pictures/mobile_browser.png"> |

4. <b>Tracing roles from commandline</b>

After each role assignment a message will be prompt to GOD's commandline which inform players ip, id and his/her role,
players should inform the GOD with thier unique id so that GOD can find who is who.  

| What GOD should see in the CLI |
|:------------------------------:|
| <img width="435" height="204" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/doc/Pictures/CLI.png"> |

## Game Rules
Mafia is a social deduction game, created by Dimitry Davidoff in 1986. The game models a conflict between two groups: an informed minority (the mafia team), and an uninformed majority (the Residents).
At the start of the game, each player is secretly assigned a role affiliated with one of these teams. The game has two alternating phases:

+ Night Phase

a night role during which those with night killing powers may covertly kill other players

All players close their eyes. The GOD then instructs all Mafias to open their eyes and acknowledge their accomplices. The mafias suggest a "victim" by silently gesturing to indicate their target and to show unanimity then Don (Mafia's head) should decide whom to be killed then close their eyes again.
A similar process occurs for other roles with nightly actions. In the case of the Detector, the GOD may indicate the target's innocence or guilt by using gestures such as nodding or head shaking.

+ Day Phase

a day role, in which surviving players debate the identities of players and vote to eliminate a suspect.

The GOD instructs players to open their eyes. Discussion ensues among the living players. At any point, a player may accuse someone of being a mafia and prompt others to vote to eliminate them. If over half of the players do so, the accused person should go to the court.Players which goes to the court may have a speech defending theirselves from not being mafia, then GOD should take votes again and this time the player with maximum vote will dead and night begins. Otherwise, the phase continues until an elimination occurs.
Dead players are not permitted to attempt to influence the remainder of the game.Because players have more freedom to deliberate, days tend to be longer than nights.

The game continues until a faction achieves its win condition; for the Residents, this usually means eliminating the whole mafia team, while for the minority this usually means reaching numerical parity with the Residents.

### Roles

#### Mafia Team
| Role | image(s) | Descriptions |
|:----:|:--------:|:------------:|
|      Don        | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Don_1.png"> <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Don_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Don_3.png"> | Don is the boss of the mafia group. At night mode Don decides whom to be killed from the mafia team.Don can't be detected by detective. |
|     Mafia       | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Mafia_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Mafia_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Mafia_3.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Mafia_4.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Mafia_5.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Mafia_6.png"> | Mafia is the simple participant of the mafia team. Mafia gets up at night and try to decide which one of the players they want to kill, detective can detect this kind of mafia in night mode. |
|     Made Man    | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Made Man_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Made Man_2.png"> | Made Man is the one of the most powerful participant of the mafia team. Made Man gets up at night and turn one of the members of city team to Mafia. |
|    Kind Wife   | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Kind Wife_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Kind Wife_2.png"> | Kind Wife is mafia team's sweetheart. After the day she died the mafia team get up and kill two suspects instead of one to take her revenge. |
|     Lawyer    | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Lawyer_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Lawyer_2.png"> | Lawyer is from mafia team. Lawyer wakes up at night and inform the GOD whom should be sued to be to the court for next day phase. |

#### City Team
| Role | image(s) | Descriptions |
|:----:|:--------:|:------------:|
|      Rebel      | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Rebel_1.png"> | Rebel is from city team which gets up at night mode and kills a person.if the victim was chosen from residents, Rebel (him/her)self may die. |
|    Doctor    | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Doctor_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Doctor_2.png"> | Doctor is a helpful participant of city team which gets up after mafia team and tries to rescue a person (or two in the first night) from mafia's shot. |
|    Detective    | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Detective_1.png"> | Detective is from city team gets up at night mode and tries to ask GOD if someone is good (Resident, Doctor, Rebel, Bulletproof) or bad(Mafia), but his/her first attempt to ask from. Don may be answered incorrect by GOD. |
|   Bulletproof   | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Bulletproof_1.png"> | Bulletproof is the most powerful resident which doesn't hurt from night shots. he/she won't die through night mode. |
|     Resident    | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_3.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_4.png"> | Resident is the typical player of the game. he/she has no power but to blame mafia in order to remove them from the game in day mode. |

## References
Icons made by <a href="https://www.flaticon.com/authors/vectors-market" title="Vectors Market">Vectors Market</a> and <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>.

Sounds from <a href="https://www.soundjay.com">Soundjay</a>.

+ [https://en.wikipedia.org/wiki/Mafia_(party_game)](https://en.wikipedia.org/wiki/Mafia_(party_game))
