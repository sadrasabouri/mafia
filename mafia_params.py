ordered_roles = ["Resident",
                 "Don",
                 "Resident",
                 "Mafia",
                 "Doctor",
                 "Detective",
                 "Mafia",
                 "Resident",
                 "Rebel",
                 "Anti-attack",
                 "Mafia",
                 "Resident",
                 "Resident",
                 "Resident",
                 "Mafia",
                 "Resident",
                 "Resident"]

nRoles = {"Don" : 1,
          "Resident" : 4,
          "Mafia" : 2,
          "Doctor" : 2,
          "Rebel" : 1,
          "Detective" : 1,
          "Anti-attack" : 1}

descriptions = {"Don" : "Don is the boss of the mafia group. At night mode Don decides whom to be killed from the mafia team.",
           "Resident" : "Resident is the typical player of the game. he/she has no power but to blame mafia in order to remove them from the game in day mode.",
           "Mafia" : "Mafia is the simple participant of the mafia team. Mafia gets up at night and try to decide which one of the players they want to kill.",
           "Doctor": "Doctor gets up after mafia team and tries to rescue a person (or two in the first night) from mafia's shot.",
           "Detective" : "Detective gets up after Doctor and tries to ask GOD if someone is good (Resident, Doctor, Rebel, Anti-attack)."
                        "or bad(Mafia), but his/her first attempt to ask from Don may be answered incorrect by GOD.",
           "Rebel" : "Rebel gets up at night mode and kills a person.if the victim was chosen from residents, Rebel (him/her)self may die.",
           "Anti-attack" : "Anti-attack doesn't hurt from night shots. he/she won't die through night mode."}

descriptions_fa = {"Don" : "دن رییس گروه مافیا است. در شب دن تصمیم می گیرد که چه کسی را از طرف تیم مافیا خارج کند",
           "Resident" : "شهروند عضو ساده شهر است. تنها قدرتی که شهروند دارد حذف افراد به واسطه رای گیری در روز است",
           "Mafia" : "مافیا عضو ساده تیم مافیا است. او هر شب بیدار می شود و به همراه مافیا دیگر عضو پیشنهادی برای حذف را به دن معرفی میکنند",
           "Doctor": "دکتر عضو تیم شهروندان است. او هر شب از خواب بیدار می شود و یک (یا ۲ در شب اول) نفر را از خطر مرگ توسط مافیا حفظ میکند",
           "Detective" : "کار آگاه عضو تیم شهروندان است. او در شب از خواب بیدار می شود و از یکی از بازیکن ها استعلام میگیرد"
                        " خدا وضعیت شخص را (مافیا بودن یا نبودن او را) به اطلاعش می رساند. ضمنا اولین استعلام کارآگاه راجع به دن"
                        "وضعیت او را مشخص نمیکند",
           "Rebel" : "شورشی عضو تیم شهروندان است. او در شب از خواب بیدار می شود و سعی میکند یکی از اعضای تیم مافیا را هدف بگیرد در صورتی که"
                    "او مافیا را به درستی تشخیص دهد مافیا خواهد مرد و در غیر این صورت شورشی در اثر غم کشتن یک شهروند خود می میرد",
           "Anti-attack" : "ضد ضربه از ضربات شب مافیا و شورشی در امان است. او هیچگاه در شب نمی میرد"}

role2fa = {"Don" : "دن",
           "Resident" : "شهروند",
           "Mafia" : "مافیا",
           "Doctor": "دکتر",
           "Detective" : "کارآگاه",
           "Rebel" : "شورشی",
           "Anti-attack" : "ضد ضربه"}
