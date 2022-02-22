# print("Kiritilgan sonning kvadratini gisoblaydigan dastur: ")
# savol = "Istalgan son kiriting "
# savol += "(dasturni toxtatmoqchi bolsangiz 'exit' deb yozing) "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat.lower() == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print("Dastur to'xtadi !")



# book = "Yoqtirgan kitobingizni kiriting "
# book += "(dasturni toxtatmoqchi bosangiz (stop) deb yozing) "
# fraza = True
# while fraza:
#     books = input(book)
#     if books.lower() == 'stop':
#         fraza = False
#     else:
#         print(books)
# print("Dastur toxtatildi !")


# print("Muzeyga xush kelibsiz !!!")
# yosh = "Yoshingiz nechida "
# yosh += "(agar muzeyga kishni hohlamasangiz (exit) yoki (quit) deb yozing) "
# fraza = True
# while fraza:
#     chegara = str(input(yosh))
#     if chegara.lower() == 'exit' or chegara.lower() == 'quit':
#         fraza = False
#     elif int(chegara) <= 7:
#         print("Kirish 2000 so'm")
#     elif int(chegara) >= 7 and int(chegara) <= 18:
#         print("Kirish 3000 so'm")
#     elif int(chegara) >= 18 and int(chegara)  <= 65:
#         print("Kirish 10000 so'm")
#     elif int(chegara) > 65:
#         print("Kirish bepul !")
# print("Kelib turing !")



savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat.lower() == 'exit':
        break
    elif int(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")