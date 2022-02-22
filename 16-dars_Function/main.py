def rezume(ism, familiya, tugulgan_yil, tugulgan_joy, email, tel_raqam):
    malunotlar = {
        'ismingiz': ism,
        'familiyangiz': familiya,
        'tugulgan yilingiz': tugulgan_yil,
        'tugulgan joyingiz': tugulgan_joy,
        'emailingiz': email,
        'telefon raqamingiz': tel_raqam
    }
    fraza = True
    while fraza:
        if ism and familiya and tugulgan_yil and tugulgan_joy and email and tel_raqam:
            fraza = False
        elif not ism and familiya and tugulgan_yil and tugulgan_joy and email and tel_raqam:
            print("malumotni toliq kiriting !")
            continue
        for key, value in malunotlar.items():
            print(f"\n{key.title()} {value}")

rezume('Samandar', 'Abdumannopov', 2003, 'Toshkent-viloyati', 'Abdumannopov.saman@gmail.com', '+99897 249 76 73')




# def numbers():
#     result = []
#     n = 1
#     while n <= 3:
#         son = int(max(input(f"{n}-son kiriting: ")))
#         result.append(son)
#         n+=1
#     print(result)
# numbers()



