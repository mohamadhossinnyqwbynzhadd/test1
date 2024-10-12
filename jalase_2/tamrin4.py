print ("salam be in barname khosh amadid\nage khsti bere marhale badi benvis 'badi'")

name_vasile = {}


def kharid_kala():
    while True:
        try:
            kala = str(input("nam kalaye mored nazar ra vared konid"))
            if kala.lower()=="badi":
                break
            hazine = input("hazine kala gheghadr ast?")
            hazine = int(hazine)
        except ValueError:
            print("lotfan adad sahih vared konid")
            continue

        if kala in name_vasile.keys():
            hazine_1 = name_vasile.get(kala) + hazine
            name_vasile.update({kala:hazine_1})
        else:
            name_vasile.update({kala:hazine})
    return name_vasile
list_kala = kharid_kala()
def magmooe_hazine():
    magmooe = 0
    for numbers in list_kala.values():
        magmooe += numbers
    return magmooe
jam_kala = magmooe_hazine()
def boodje():
    while True:
         boodje_karbar = input("boodje shoma cheghadr ast?")                  
         try:
             boodje_karbar = int(boodje_karbar)
             break
         except ValueError:
             print("lotfan adad sahih vared konid!")
             continue
    baghi_mande = boodje_karbar - jam_kala
    if 0 >baghi_mande:
        print(f"---------------\nHazine kala ha : {jam_kala}")
        print ("hazine kala ha bishtar az boodje shoma bood")
    else:
        print ("shoma mi tavanid pardakht konid:)")
        print(f"-----------\nhazine kala ha : {jam_kala}")
        print(f"hazine baghi mande : {baghi_mande}")
    return
boodje()          
