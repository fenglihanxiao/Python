"""
    1. name:            startswith
    2. nick_name        find
    3. gender           ==
    4. blood            ==
    5. native           find
    6. id_card          slice and comparison
"""
db_infos = [
    {
        "name":         "JamRichard Li",
        "nick_name":    "fengond ster",
        "gender":        1,
        "blood":        "B",
        "native":       "SichuanEngland",
        "id_card":      "510103198604260017"
    },

    {
        "name":         "Amy Han",
        "nick_name":    "lover",
        "gender":       0,
        "blood":        "A",
        "native":       "Beijin",
        "id_card":      "510103198610300018"
    },

    {
        "name":         "James Bond",
        "nick_name":    "killer yonder",
        "gender":       1,
        "blood":        "B",
        "native":       "Sucker England",
        "id_card":      "510103197804260017"
    },
    ]

for person in db_infos:
    name = person["name"]
    nick_name = person["nick_name"]
    gender = person["gender"]
    blood = person["blood"]
    native = person["native"]
    id_card = person["id_card"]
    # Check conditions
    #   1. All the conditions meet -> print info
    #   2. PREFERRED WAY:If one condition does not meet, then iterate to next
    #       1. goes to 2.2
    if not name.startswith("Jam"):
        continue

    if name.find("ond") == -1 and nick_name.find("ond") == -1:
        continue

    if gender != 1:
        continue

    if blood.lower() != "b":
        continue

    if native.lower().find("england") == -1:
        continue

    # id_card: XXXXXX;XXXX;XX;XXXX
    if int(id_card[6:10]) < 1975 or int(id_card[6:10]) > 1978:
        continue

    # 2.2->if program goes to here, it invalidate all six condition.
    # As a result, we find the target
    genders = {1: "Male", 0: "Female", -1: "NA"}

    print("name=" + name + ",nick_name=" + nick_name + ",gender="
          + genders[gender] + ",blood=" + blood + ",native=" + native + ",id_card=" + id_card)
