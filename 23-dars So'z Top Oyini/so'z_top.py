import random as r
from uzwords import words

def pc_soz():
    random_soz = r.choice(words)
    fraza = True

    while fraza:
        if "-" in random_soz or " " in random_soz: # Toki bo'sh joy yoki chiziqcha yo'q soz bergunicha tikl qaytarilaveradi
            random_soz = r.choice(words)
        else:
            fraza = False
    return random_soz.upper()

def result(taxmin, random_soz): # Foydalanuvchi kiritgan hariflar bilan random bergan so'z solishtiriladi
    taxminlar = "" # Togri kelgan harflar joylab boriladi togri kelmaganlarini orniga - chiziqcha qoladi
    for harflar in random_soz:
        if harflar in taxmin:
            taxminlar += harflar
        else:
            taxminlar += "-"
    return taxminlar

def oyin():
    random_soz = pc_soz() # random bergan so'zni o'zgaruvchiga oldim
    random_harflar = set(random_soz) # random bergan so'zni takrorlanmas qilib oldim
    user_harflar = ""
    print(f"Мен {len(random_soz)} та харифдан иборат соз ойладим топа оласизми?")

    while len(random_harflar)>0: # Har bitta topilgan harf evaziga 1 tadan length kamayib boraveradi va tikl toxtaydi
        print(result(user_harflar, random_soz)) # O'yinni ko'rinishini chaqirdik
        if len(user_harflar)>0:
            print(f"Шу вактгача киритган хартфларингиз: {user_harflar}")

        harf = input("Харф киритинг: ").upper()
        if harf in user_harflar:
            print("Бу харф киритилган бошка харф киритинг !")
            continue
        elif harf in random_soz:
            random_harflar.remove(harf) # Topilgan harfni orniga joylanadi
            print(f"{harf} харфи топилди")
        else:
            print("Бундай харф йок")

        user_harflar += harf
    print(f"Табриклаймиз! {random_soz} созини {len(user_harflar)} та урунишда топдингиз!!!")

oyin()