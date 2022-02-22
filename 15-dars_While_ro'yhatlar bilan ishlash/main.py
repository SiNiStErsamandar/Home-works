# buyurtmalar = []
# print("Hohlagan buyurtmangizni kiriting: ")
# n=1
# while True:
#     savol = f"{n}-buyurtmani kiriting: "
#     buyurtma = input(savol)
#     buyurtmalar.append(buyurtma)
#     buyurtma = input("Yana buyurtma berasizmi? (ha/yo'q) ")
#     if buyurtma.lower() == 'ha':
#         n+=1
#         continue
#     else:
#         break
# print(buyurtmalar)



# print("Bozorlik qilamiz !")
# bozorlik = {}
# fraza = True
# while fraza:
#     masalliq = input("Masalliq nomini kiriting: ")
#     narhi = input(f"{masalliq.title()} narhi qancha : ")
#     bozorlik[masalliq] = int(narhi)

#     savol = input("Bozorlikni davom ettiramizmi (ha/yo'q): ")
#     if savol.lower() == "yo'q":
#         fraza = False
#     elif savol.lower() == "ha":
#         continue

# for masalliq, narhi in bozorlik.items():
#     print(f"{masalliq.title()} narhi {narhi}")



bozor = {
    'non': 3000,
    'kalbasa': 20000,
    'olma': 12000,
    'cola': 10000,
    "go'sht": 50000,
    'shirinlik': 25000
}
print("Hohlagan buyurtmangizni kiriting: ")
bori = []
fraza = True
while fraza:
    buyurtma = input("Mahsulot nomi: ")
    bori.append(buyurtma)
    savol = input("Bozorlikni davom etasizmi (ha/yo'q) deb yozing: ")
    if savol.lower() == 'ha':
        continue
    elif savol.lower() == "yo'q":
        fraza = False
for key, value in bozor.items():
    if bori == key:
        print(f"{bori} narhi {value}")
    elif bori != key:
        print("Bizda bunday mahsulotlar mavjut emas !")  