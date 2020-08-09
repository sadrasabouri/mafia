ordered_roles = ["Resident",
                 "Don",
                 "Resident",
                 "Mafia",
                 "Doctor",
                 "Detector",
                 "Mafia",
                 "Resident",
                 "Rebel",
                 "Anti-attck",
                 "Mafia",
                 "Resident"]

nRoles = {"Don" : 1,
          "Resident" : 4,
          "Mafia" : 2,
          "Doctor" : 2,
          "Rebel" : 1,
          "Detective" : 1,
          "Anti-attack" : 1}

descriptions = {"Don" : "Don is the boss of the mafia group. At night mode he'll decide whom to be killed from mafia team.",
           "Resident" : "Resident is the most simple player in the mafia game. he/she has no power but to blame mafia in order to remove them from game in day mode.",
           "Mafia" : "Mafia is the simple mafia player. they'll get up at night and try to decide which one of the peoples they want to kill.",
           "Doctor": "Doctor gets up after mafia team and try to rescue a person (or two in first night) from mafia's attack.",
           "Detector" : "Detector gets up after Doctor and try to ask GOD if someone is good (Resident, Doctor, Rebel, Anti-attack) <br>"
                        "or bad(Mafia), but his/her first attempt to ask from Don may be answered incorrect by GOD.",
           "Rebel" : "Rebel gets up at night mode and kill a person.if the victim was chosen from residents Rebel (him/her)self may die",
           "Anti-attack" : "Anti-attack won't hurt from night shoots. he/she won't die through night mode."}

role2fa = {"Don" : "دن",
           "Resident" : "شهروند",
           "Mafia" : "مافیا",
           "Doctor": "دکتر",
           "Detector" : "کارآگاه",
           "Rebel" : "شورشی",
           "Anti-attack" : "ضد ضربه"}
