# lugat = {
#     'dodam': 'borsh',
#     'opam': 'mosh',
#     'katta_opacham': 'shashlik',
#     'kichkina_opacham': 'baliq',
#     'men': 'tandir',
#     'men': 'tandir'
# }

# for qiymat in set(lugat.values()):
#     print(f"Qiymat {qiymat}")

# python = {
#     'str': 'faqat yozuvlarni qabul qiladi',
#     'int': 'faqat sonlarni qabul qiladi',
#     'float': 'faqat bolinuvchi sonlarni qabul qiladi',
#     'bool': 'bu operator faqat true va false yani rost va yolgon degani',
#     'o`zgaruvchi': 'quti vazifasibi otab beradi',
#     'ro`yxat': 'xar xil turdagi malumotlarni ichida jamlashi miumkin',
#     'for': 'uchun manosini anglatadi',
#     'if': 'agarda manosini anglatadi',
#     'else': 'yo`qsa manosini anglatadi',
#     'input': 'foydalanuvchi tomonidan kiritilishi uchun funcsiya',
# }

# for kalit, qiymat, in sorted(python.items()):
#     print(f"{kalit.capitalize()} - {qiymat.capitalize()}")


# python = {
#     'str': 'faqat yozuvlarni qabul qiladi',
#     'int': 'faqat sonlarni qabul qiladi',
#     'float': 'faqat bolinuvchi sonlarni qabul qiladi',
#     'bool': 'bu operator faqat true va false yani rost va yolgon degani',
#     'o`zgaruvchi': 'quti vazifasibi otab beradi',
#     'ro`yxat': 'xar xil turdagi malumotlarni ichida jamlashi miumkin',
#     'for': 'uchun manosini anglatadi',
#     'if': 'agarda manosini anglatadi',
#     'else': 'yo`qsa manosini anglatadi',
#     'input': 'foydalanuvchi tomonidan kiritilishi uchun funcsiya',
# }

# for kalit, qiymat, in sorted(python.items()):
#     print(kalit.upper(), qiymat.capitalize())




# python = {
#     'str': 'faqat yozuvlarni qabul qiladi',
#     'int': 'faqat sonlarni qabul qiladi',
#     'float': 'faqat bolinuvchi sonlarni qabul qiladi',
#     'bool': 'bu operator faqat true va false yani rost va yolgon degani',
#     'o`zgaruvchi': 'quti vazifasibi otab beradi',
#     'ro`yxat': 'xar xil turdagi malumotlarni ichida jamlashi miumkin',
#     'for': 'uchun manosini anglatadi',
#     'if': 'agarda manosini anglatadi',
#     'else': 'yo`qsa manosini anglatadi',
#     'input': 'foydalanuvchi tomonidan kiritilishi uchun funcsiya',
# }

# user = str(input("Kod nomini kiriting : "))

# for kalit, qiymat in python.items():
#     if user.lower() in kalit:
#         print(f"{user}ning manosi {python[user]}")
#     elif user.lower() not in kalit:
#         print("Kechirasiz bunday malumot yoq")





# menu = {
#     'osh': 50000,
#     'manti': 10000,
#     'choy': 1000,
#     'coffe': 5000,
#     'salat': 15000,
#     'tovuq': 60000,
#     'shashlik': 8000,
#     'muzqaymoq': 12000,
#     'suv': 1.500,
#     'mevalar': 20000,
# }

# user = str(input("1-buyurtma kiriting : "))
# user1 = str(input("2-buyurtma kiriting : "))
# user2 = str(input("3-buyurtma kiriting : "))
# mijoz = user, user1, user2,
# for xoranda in mijoz:
#     if xoranda.lower() in menu:
#         print(f"{xoranda} narxi {menu[xoranda]}")
#     else:
#         print("Bizda bunday nom yoq!")


# shaxs0 = {
#     'ismi': 'Mbu Mbdulloh Muhammad ibn Ismoil',
#     'yili': 810,
#     'manzil': 'Buxoro',
#     'yashagan': 60,
#     'asarlar': 'Al-jome as-sahih Al-abab al-mufrad At-tarix al-kabir At-tarix as-sag`ir'
# }


# shaxs1 = {
#     'ismi': 'Abdula Qodiriy',
#     'yili': 1894,
#     'manzil': 'Toshkent',
#     'yashagan': 44,
#     'asarlar': 'O`tgan kunlar Mehrobdan Chayon Obid ketmon'
# }

# shaxs2 = {
#     'ismi': 'Erkin Vohidov',
#     'yili': 1936,
#     'manzil': 'Farg`ona',
#     'yashagan': 80,
#     'asarlar': 'Tong nafasi Qo`shiqlarim sizga O`zbegim Qiziquvchan Matmusa'
# }

# shaxs3 = {
#     'ismi': 'Alisher Navoiy',
#     'yili': 1441,
#     'manzil': 'Xirot',
#     'yashagan': 60,
#     'asarlar': 'Xamsa Lison ut-Tayr Mahbub Al-Qulub Lorem ipsum'
# }

# shahslar = [shaxs0, shaxs1, shaxs2, shaxs3]
# for shahs in shahslar:
#     print(f"{shahs['ismi']} {shahs['yili']}-yilda {shahs['manzil']} tavallud topgan. {shahs['yashagan']} umr k'rgan")
# for shaxs in shahslar:
#     print(f"{shaxs['ismi']} yozgan asarlar: \
#         {shaxs['asarlar']}")




# kinolar = {
#     'ali': []
# }

# dostlar1 = input("1-Kino : ")
# dostlar2 = input("2-Kino : ")
# dostlar3 = input("3-Kino : ")

# dost = dostlar1, dostlar2, dostlar3
# # for dos in dost:
# kinolar["ali"].append(dost)
# print(kinolar)



# davlatlar = {
#     'davlat1': {'nomi': 'toshkent ',
#             'hududi': [448978, 'kv.km '],
#             'aholi': 33000000,
#             'pul birligi': ' so`m',
#             },
    
#     'davlat2': {'nomi': 'rpssiya ',
#             'hududi': [17098246, 'kv.km '],
#             'aholi': 144000000,
#             'pul birligi': ' rubl',
#             },

#     'davlat3': {'nomi': 'aqsh ',
#             'hududi': [9631418, 'kv.km '],
#             'aholi': 327000000,
#             'pul birligi': ' dollar',
#             }
# }

# for key, value in davlatlar.items():
#     print(f"{key.title()} {value['nomi']}"
#         f"{value['hududi']}"
#         f"{value['aholi']}"
#         f"{value['pul birligi']}.")






davlatlar = {
    'toshkent': {'nomi': 'toshkent ',
            'hududi': [448978, 'kv.km '],
            'aholi': 33000000,
            'pul birligi': ' so`m',
            },
    
    'rossiya': {'nomi': 'rossiya ',
            'hududi': [17098246, 'kv.km '],
            'aholi': 144000000,
            'pul birligi': ' rubl',
            },

    'aqsh': {'nomi': 'aqsh ',
            'hududi': [9631418, 'kv.km '],
            'aholi': 327000000,
            'pul birligi': ' dollar',
            }
}

user = str(input("Hohlagan davlatingizni kiriting : "))
for key, value in davlatlar.items():
    if user.lower() == key:
        print(f"{value['nomi'].title()}"
            f"{value['hududi']}"
            f"{value['aholi']}"
            f"{value['pul birligi']}.")
    else:
        print("Kechirasiz bunday davlat ro'yxatimizda yo'q !")
        

