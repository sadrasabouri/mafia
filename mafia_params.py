ordered_roles = ["Resident",
                 "Don",
                 "Resident",
                 "Mafia",
                 "Doctor",
                 "Detective",
                 "Mafia",
                 "Resident",
                 "Rebel",
                 "Bulletproof",
                 "Resident",
                 "Mafia",
                 "Resident",
                 "Resident",
                 "Mafia",
                 "Resident",
                 "Resident",
                 "Mafia",
                 "Resident",
                 "Resident"]

nRoles = {"Boxer" : 2,
          "Bride" : 3,
          "Bulletproof" : 4,
          "Bus Driver" : 2,
          "Chef" : 3,
          "Curious Kid" : 2,
          "Detective" : 3,
          "Doctor" : 6,
          "Don" : 3,
          "Genie" : 2,
          "Grandma" : 2,
          "Groom" : 4,
          "Insane" : 2,
          "Jailer" : 2,
          "Judge" : 2,
          "Kind Wife" : 2,
          "Lawyer" : 2,
          "Made Man" : 2,
          "Mafia" : 6,
          "Magician" : 3,
          "Miller" : 3,
          "Postman" : 2,
          "Rebel" : 3,
          "Resident" : 8,
          "Student" : 2,
          "Undercover Cop" : 2
          }

descriptions = {"Don" : "Don is the boss of the mafia group. At night mode Don decides whom to be killed from the mafia team."
                        "Don can't be detected by detective.",
           "Resident" : "Resident is the typical player of the game. he/she has no power but to blame mafia in order to remove "
                        "them from the game in day mode.",
           "Mafia" : "Mafia is the simple participant of the mafia team. Mafia gets up at night and try to decide which one of"
                        "the players they want to kill, detective can detect this kind of mafia in night mode.",
           "Doctor": "Doctor is a helpful participant of city team which gets up after mafia team and tries to rescue a person"
                        " (or two in the first night) from mafia's shot.",
           "Detective" : "Detective is from city team gets up at night mode and tries to ask GOD if someone is good"
                        " (Resident, Doctor, Rebel, Bulletproof) or bad(Mafia), but his/her first attempt to ask from"
                        " Don may be answered incorrect by GOD.",
           "Rebel" : "Rebel is from city team which gets up at night mode and kills a person.if the victim was chosen from"
                        " residents, Rebel (him/her)self may die.",
           "Bulletproof" : "Bulletproof is the most powerful resident which doesn't hurt from night shots. he/she won't die"
                        " through night mode."}

descriptions_fa = {"Don" : "اين نقش سردسته تيم مافيا مي باشد و مسئوليت تيم مافيا بر عهده دُن است.امتياز حائز اهميتی که دُن در بازی دارد اين است که استعلامش توسط کاراگاه همانند شهروندان منفی میباشد.",
           "Resident" : "شهروند عضو ساده شهر است. تنها قدرتی که شهروند دارد حذف افراد به واسطه رای گیری در روز است",
           "Mafia" : "از اعضای تیم مافیا میباشد و اگر کارآگاه از او استعلام بگیرد، استعلامش مثبت می شود",
           "Doctor": "دکتر يکی از اعضای تیم شهروند ميباشد که در فاز شب به فرمان خدای بازی چشم هايش را باز کرده و ميتواند خود و يا يکی از بازيکنان را از حذف شدن و کشته شدن در فاز شب بازی نجات دهد.",
           "Detective" : "کارآگاه يکی از اعضای تیم شهروند ميباشد که در فاز شب چشم هايش را باز کرده و ميتواند از خدای بازی هويت يکی از افراد بازی را بپرسد ، و خدا با اشاره بله يا خیر به کاراگاه ميگويد که فرد استعلام شده جزو اعضای مافيا هست يا نه",
           "Rebel" : "از اعضای تیم شهروند میباشد و در فاز شب میتواند کسی را که فکر میکند مافیا است را هدف قرار دهد اگر شخص مافیا بود خواهد مرد.اما اگر شورشی به اشتباه یک شهروند را هدف قرار دهد خودش خواهد مرد.",
           "Bulletproof" : "ضد ضربه قوی ترين شهروند بازی ميباشد ،و از هر تير مافیا در فاز شب در امان ميباشد.بنابرين ضد ضربه توسط مافيا در فاز شب قابل کشته شدن نميباشد"}

role2fa = {"Don" : "دن",
           "Resident" : "شهروند",
           "Mafia" : "مافیا",
           "Doctor": "دکتر",
           "Detective" : "کارآگاه",
           "Rebel" : "شورشی",
           "Bulletproof" : "ضد ضربه"}
