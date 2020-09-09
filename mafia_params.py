ordered_roles = ["Resident",
                 "Don",
                 "Resident",
                 "Detective",
                 "Doctor",
                 "Hit Man",
                 "Rebel",
                 "Resident",
                 "Mafia",
                 "Bulletproof",
                 "Resident",
                 "Mafia",
                 "Resident",
                 "Resident",
                 "Mafia",
                 "Doctor",
                 "Chef",
                 "Mafia",
                 "Detective",
                 "Miller",
                 "Mafia",
                 "Undercover Cop",
                 "Grandma",
                 "Mafia",
                 "Student",
                 "Postman",
                 "Mafia",
                 "Clown",
                 "Resident",
                 "Mafia"
                 "Resident",
                 "Resident"]

nRoles = {"Boxer" : 2,
          "Bride" : 5,
          "Bulletproof" : 9,
          "Bus Driver" : 3,
          "Chef" : 3,
          "Clown" : 2,
          "Curious Kid" : 2,
          "Detective" : 3,
          "Doctor" : 10,
          "Don" : 4,
          "Genie" : 2,
          "Grandma" : 2,
          "Groom" : 4,
          "Hit Man" : 2,
          "Insane" : 3,
          "Jailer" : 2,
          "Judge" : 6,
          "Kind Wife" : 4,
          "Lawyer" : 3,
          "Made Man" : 2,
          "Mafia" : 9,
          "Magician" : 4,
          "Miller" : 3,
          "Postman" : 3,
          "Priest" : 3,
          "Rebel" : 3,
          "Reporter" : 6,
          "Resident" : 21,
          "Serial Killer" : 6,
          "Student" : 2,
          "Undercover Cop" : 2
          }

descriptions = {"Boxor" : "Boxor is a member of mafia team. Boxor hits one of the players at night and the one"
                          " who hited Can't deffend oneself during day phase due to it's hit effect.",
                "Bride" : "Bride is a member of city team. Bride has been engaged to Groom recently at nigh both of"
                        " them will get up and see each other after death of each one of them, other one can kill"
                        " anyone as a revenge of his/her sweetheart at night phase.",
                "Bulletproof" : "Bulletproof is the most powerful resident which doesn't hurt from night shots. he/she won't die"
                                " through night phase.",
                "Bus Driver" : "Bus Driver is city team member. He/She can switch two player which means each shot/question"
                               " from first one will hurt/asked from second one.",
                "Chef" : "Chef is critical member of city team. After his/her death city team should win at last after 3 days.",
                "Clown" : "Clown is a member of city team. Clown forces someone to reveal his/her role for another players."
                          " Clown can do this just for one time and this should take place at night, GOD should be informed"
                          " whos role to be reavealed.",
                "Curious Kid" : "He/She is a member of city team which can open his/her eyes and spy on mafias in the way"
                          " that no one can see him/her.",
                "Detective" : "Detective is from city team gets up at night phase and tries to ask GOD if someone is good"
                                " (Resident, Doctor, Rebel, Bulletproof) or bad(Mafia), but his/her first attempt to ask from"
                                " Don may be answered incorrect by GOD.",
                "Doctor": "Doctor is a helpful participant of city team which gets up after mafia team and tries to rescue a person"
                            " (or two in the first night) from mafia's shot.",
                "Don" : "Don is the boss of the mafia group. At night phsae Don decides whom to be killed from the mafia team."
                        "Don can't be detected by detective.",
                "Genie" : "Genie is a kind member of city team despite his/her name. Genie selects a player at night and GOD "
                          "will ask the player to wish something and his/her wish will come true. Genie can use his/her power"
                          " just three time in a game.",
                "Grandma" : "Grandma with gun is a frightening member of city team. She will kill anyone who tries to kill her"
                            " at night. Mafia and other roles with kiling power should be aware of her.",
                "Groom" : "Groom is a member of city team. Groom has been engaged to Bride recently at nigh both of"
                        " them will get up and see each other after death of each one of them, other one can kill"
                        " anyone as a revenge of his/her sweetheart at night phase.",
                "Hit Man" : "Hit Man is a rather powerful member of mafia team. His/Her shots won't fail even if the doctor save"
                            " or the victim is Bulletproof. Hit Man can use his shot only one time during the game his shot will"
                            " be replaced by one of mafia's night shot.",
                "Insane" : "Insane is a member of city team. GOD will infrom Insane who is aiming at his/her neighbors (left hand"
                           " player or right hand player).",
                "Jailer" : "Jailer is a member of city team. Jailer can bust any player at night phase, one who has been busted won't"
                           " play at earlier day phase just for a night.",
                "Judge" : "Judge is a member of city team. Judge can reveal his role and decide to kill a player at day phase, Judge"
                          " can use his/her power only once during the game.",
                "Kind Wife" : "Kind Wife is mafia team's sweetheart. After the day she died the mafia team get up and kill two suspects"
                              " instead of one to take her revenge.",
                "Lawyer" : "Lawyer is from mafia team. Lawyer wakes up at night and inform the GOD whom should be sued to be to the court"
                           " for next day phase.",
                "Made Man" : "Made Man is the one of the most powerful participant of the mafia team. Made Man gets up at night and turn"
                             " one of the members of city team to Mafia.",
                "Mafia" : "Mafia is the simple participant of the mafia team. Mafia gets up at night and try to decide which one of"
                          "the players they want to kill, detective can detect this kind of mafia in night phase.",
                "Magician" : "Magician is member of city team. He/She decides to kill or save a player during night and can use his/her"
                             "power just once during the game.",
                "Miller" : "Miller is a member of city team. When Detective ask GOD about Millers role the result will be bad(Mafia) so"
                           " Detective will be confused about Millers role and asume he/she as a mafia team member.",
                "Postman" : "Postman is a member of city team. After Postman's death he/she can select a player to die with him/her."
                            " With this power Postman can help city team by killing a mafia member.",
                "Priest" : "",
                "Rebel" : "Rebel is from city team which gets up at night phase and kills a person.if the victim was chosen from"
                                " residents, Rebel (him/her)self may die.",
                "Reporter" : "Reporter is a city team member. GOD will inform Reporter who was chosen by Made Man to become Mafia.",
                "Resident" : "Resident is the typical player of the game. he/she has no power but to blame mafia in order to remove "
                             "them from the game in day phase.",
                "Serial Killer" : "Serial Killer is a seperate team. He/She wakes up once each two night and shot a player."
                                  " Serial Killer will win if He/She is in last three players.",
                "Student" : "Student is a innocent city team member. After His/Her death, players will kill two players at day court.",
                "Undercover Cop" : "Undercover Cop is a member of city team but he/she will act just like mafia (wakes up at night)"
                                   " and decide whome to be killed)."}

descriptions_fa = {"Boxor" : "", "Bride" : "", "BusDriver" : "", "Chef" : "", "Clown" : "", "Curious Kid" : "", "Genie" : "",
            "Grandma" : "", "Groom" : "", "Hit Man" : "", "Insane" : "", "Jailer" : "", "Judge" : "", "Kind Wife" : "",
            "Lawyer" : "", "Made Man" : "", "Magician" : "", "Miller" : "", "Postman" : "", "Priest" : "",
            "Reporter" : "", "Serial Killer" : "", "Student" : "", "Undercover Cop" : "",
           "Don" : "اين نقش سردسته تيم مافيا مي باشد و مسئوليت تيم مافيا بر عهده دُن است.امتياز حائز اهميتی که دُن در بازی دارد اين است که استعلامش توسط کاراگاه همانند شهروندان منفی میباشد.",
           "Resident" : "شهروند عضو ساده شهر است. تنها قدرتی که شهروند دارد حذف افراد به واسطه رای گیری در روز است",
           "Mafia" : "از اعضای تیم مافیا میباشد و اگر کارآگاه از او استعلام بگیرد، استعلامش مثبت می شود",
           "Doctor": "دکتر يکی از اعضای تیم شهروند ميباشد که در فاز شب به فرمان خدای بازی چشم هايش را باز کرده و ميتواند خود و يا يکی از بازيکنان را از حذف شدن و کشته شدن در فاز شب بازی نجات دهد.",
           "Detective" : "کارآگاه يکی از اعضای تیم شهروند ميباشد که در فاز شب چشم هايش را باز کرده و ميتواند از خدای بازی هويت يکی از افراد بازی را بپرسد ، و خدا با اشاره بله يا خیر به کاراگاه ميگويد که فرد استعلام شده جزو اعضای مافيا هست يا نه",
           "Rebel" : "از اعضای تیم شهروند میباشد و در فاز شب میتواند کسی را که فکر میکند مافیا است را هدف قرار دهد اگر شخص مافیا بود خواهد مرد.اما اگر شورشی به اشتباه یک شهروند را هدف قرار دهد خودش خواهد مرد.",
           "Bulletproof" : "ضد ضربه قوی ترين شهروند بازی ميباشد ،و از هر تير مافیا در فاز شب در امان ميباشد.بنابرين ضد ضربه توسط مافيا در فاز شب قابل کشته شدن نميباشد"}

role2fa = {"Boxer" : "بوکسور",
          "Bride" : "عروس",
          "Bulletproof" : "ضدضربه",
          "Bus Driver" : "راننده اتوبوس",
          "Chef" : "آشپز",
          "Clown" : "دلقک",
          "Curious Kid" : "کودک کنجکاو",
          "Detective" : "کارآگاه",
          "Doctor" : "دکتر",
          "Don" : "دن",
          "Genie" : "غول چراغ جادو",
          "Grandma" : "مادربزرگ با اسلحه",
          "Groom" : "داماد",
          "Hit Man" : "آدم کش",
          "Insane" : "دیوانه",
          "Jailer" : "زندان بان",
          "Judge" : "قاضی",
          "Kind Wife" : "همسر مهربان",
          "Lawyer" : "وکیل",
          "Made Man" : "آدم اجیر کن",
          "Mafia" : "مافیا",
          "Magician" : "جادوگر",
          "Miller" : "آسیابان",
          "Postman" : "پست چی",
          "Priest" : "کشیش",
          "Rebel" : "شورشی",
          "Reporter" : "خبرنگار",
          "Resident" : "شهروند",
          "Serial Killer" : "قاتل سریالی",
          "Student" : "دانش آموز",
          "Undercover Cop" : "پلیس مخفی"}
