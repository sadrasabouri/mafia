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
|      Don        | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Don_1.png"> <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Don_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Don_3.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Don_4.png"> | Don is the boss of the mafia group. At night mode Don decides whom to be killed from the mafia team.Don can't be detected by detective. |
|     Hit Man    | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Hit Man_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Hit Man_2.png"> | Hit Man is a rather powerful member of mafia team. His/Her shots won't fail even if the doctor save or the victim is Bulletproof. Hit Man can use his shot only one time during the game his shot will be replaced by one of mafia's night shot. |
|     Made Man    | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Made Man_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Made Man_2.png"> | Made Man is the one of the most powerful participant of the mafia team. Made Man gets up at night and turn one of the members of city team to Mafia. |
|    Kind Wife   | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Kind Wife_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Kind Wife_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Kind Wife_3.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Kind Wife_3.png"> | Kind Wife is mafia team's sweetheart. After the day she died the mafia team get up and kill two suspects instead of one to take her revenge. |
|     Mafia       | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Mafia_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Mafia_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Mafia_3.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Mafia_4.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Mafia_5.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Mafia_6.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Mafia_7.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Mafia_8.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Mafia_9.png"> | Mafia is the simple participant of the mafia team. Mafia gets up at night and try to decide which one of the players they want to kill, detective can detect this kind of mafia in night mode. |

#### City Team
| Role | image(s) | Descriptions |
|:----:|:--------:|:------------:|
|      Rebel      | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Rebel_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Rebel_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Rebel_3.png"> | Rebel is from city team which gets up at night mode and kills a person.if the victim was chosen from residents, Rebel (him/her)self may die. |
|    Doctor    | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Doctor_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Doctor_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Doctor_3.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Doctor_4.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Doctor_5.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Doctor_6.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Doctor_7.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Doctor_8.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Doctor_9.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Doctor_10.png"> | Doctor is a helpful participant of city team which gets up after mafia team and tries to rescue a person (or two in the first night) from mafia's shot. |
|    Detective    | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Detective_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Detective_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Detective_3.png"> | Detective is from city team gets up at night mode and tries to ask GOD if someone is good (Resident, Doctor, Rebel, Bulletproof) or bad(Mafia), but his/her first attempt to ask from. Don may be answered incorrect by GOD. |
|   Bulletproof   | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Bulletproof_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Bulletproof_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Bulletproof_3.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Bulletproof_4.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Bulletproof_5.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Bulletproof_6.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Bulletproof_7.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Bulletproof_8.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Bulletproof_9.png"> | Bulletproof is the most powerful resident which doesn't hurt from night shots. he/she won't die through night mode. |
|      Bride     | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Bride_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Bride_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Bride_3.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Bride_4.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Bride_5.png"> | Bride is a member of city team. Bride has been engaged to Groom recently at nigh both of them will get up and see each other after death of each one of them, other one can kill anyone as a revenge of his/her sweetheart at night phase. |
|      Groom     | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Groom_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Groom_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Groom_3.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Groom_4.png"> | Groom is a member of city team. Groom has been engaged to Bride recently at nigh both of them will get up and see each other after death of each one of them, other one can kill anyone as a revenge of his/her sweetheart at night phase. |
|       Chef     | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Chef_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Chef_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Chef_3.png"> | Chef is critical member of city team. After his/her death city team should win at last after 3 days. |
|      Miller     | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Miller_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Miller_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Miller_3.png"> | Miller is a member of city team. When Detective ask GOD about Millers role the result will be bad(Mafia) so Detective will be confused about Millers role and asume he/she as a mafia team member. |
|  Undercover Cop | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Undercover Cop_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Undercover Cop_2.png"> | Undercover Cop is a member of city team but he/she will act just like mafia (wakes up at night) and decide whome to be killed). |
|     Reporter    | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Reporter_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Reporter_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Reporter_3.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Reporter_4.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Reporter_5.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Reporter_6.png"> | Reporter is a city team member. GOD will inform Reporter who was chosen by Made Man to become Mafia. |
|     Grandma     | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Grandma_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Grandma_2.png"> | Grandma with gun is a frightening member of city team. She will kill anyone who tries to kill her at night. Mafia and other roles with kiling power should be aware of her. |
|      Student    | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Student_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Student_2.png"> | Student is a innocent city team member. After His/Her death, players will kill two players at day court. |
|      Postman    | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Postman_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Postman_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Postman_3.png"> | Postman is a member of city team. After Postman's death he/she can select a player to die with him/her. With this power Postman can help city team by killing a mafia member. |
|       Clown     | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Clown_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Clown_2.png"> | Clown is a member of city team. Clown forces someone to reveal his/her role for another players. Clown can do this just for one time and this should take place at night, GOD should be informed whos role to be reavealed. |
|     Resident    | <img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_1.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_2.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_3.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_4.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_5.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_6.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_7.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_8.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_9.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_10.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_11.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_12.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_13.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_14.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_15.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_16.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_17.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_18.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_19.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_20.png"><img width="100" height="100" src="https://raw.githubusercontent.com/sadrasabouri/mafia/master/static/images/roles/Resident_21.png"> | Resident is the typical player of the game. he/she has no power but to blame mafia in order to remove them from the game in day mode. |

## References
Icons made by <a href="https://www.flaticon.com/authors/vectors-market" title="Vectors Market">Vectors Market</a> and <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>.

Sounds from <a href="https://www.soundjay.com">Soundjay</a>.

+ [https://en.wikipedia.org/wiki/Mafia_(party_game)](https://en.wikipedia.org/wiki/Mafia_(party_game))
