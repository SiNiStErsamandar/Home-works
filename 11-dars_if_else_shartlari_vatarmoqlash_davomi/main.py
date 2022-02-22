# juft_son = int(input("Juft son kiriting : "))

# if juft_son % 2 == 0:
#     print("Raxmat")
# else:
#     print("Bu juft son emas !")


# odam = int(input("Yoshingiz nechida ?: "))

# if odam < 4 or odam > 60:
#     print("Cipta bepul !")
# elif odam < 18:
#     print("Chipta narxi 10000 so'm")
# elif odam > 18:
#     print("Chipta narxi 20000")
# else:
#     print("Yoshingizni kirtmadingiz !!!")


# numbers1 = float(input("Brinchi sonni kiriting : "))
# numbers2 = float(input("Ikkinchi sonni kiriting : "))

# if numbers1 < numbers2:
#     print(f'{numbers1}<{numbers2}')
# elif numbers1 > numbers2:
#     print(f'{numbers1}>{numbers2}')
# # else:
#     print(f'{numbers1}=={numbers2}')


# mahsulotlar = ['sut', 'kalbasa', 'sasiska', 'tuxum', 'tovuq', 'go`sht', 'olma', 'tarvuz', 'qovun', 'qaymoq']
# savat = []
# print("5 ta maxsulot kiriting")
# buyurtma1 = input("1-buyurtma : ")
# buyurtma2 = input("2-buyurtma : ")
# buyurtma3 = input("3-buyurtma : ")
# buyurtma4 = input("4-buyurtma : ")
# buyurtma5 = input("5-buyurtma : ")

# buyurtma = buyurtma1, buyurtma2, buyurtma3, buyurtma4, buyurtma5

# savat = buyurtma

# for javob in savat:
#     if javob in mahsulotlar:
#         print(f'{javob} do`konimizda bor')
#     else:
#         print(f'{javob} do`konimizda yo`q')



# mahsulotlar = ['sut', 'kalbasa', 'sasiska', 'tuxum', 'tovuq', 'go`sht', 'olma', 'tarvuz', 'qovun', 'qaymoq']
# bor_mahsulotlar = []
# yoq_mahsulotlar = []
# print("5 ta maxsulot kiriting")
# buyurtma1 = input("1-buyurtma : ")
# buyurtma2 = input("2-buyurtma : ")
# buyurtma3 = input("3-buyurtma : ")
# buyurtma4 = input("4-buyurtma : ")
# buyurtma5 = input("5-buyurtma : ")

# buyurtma = buyurtma1, buyurtma2, buyurtma3, buyurtma4, buyurtma5

# savat = buyurtma

# for javob in savat:
#     if javob in mahsulotlar:
#         bor_mahsulotlar.append(print('Do`konimizda siz so`ragan barcha mahsulotlar bor'))
#     if javob not in mahsulotlar:
#         yoq_mahsulotlar.append(print(f'{javob} do`konimizda quyidagi mahsulotlar yoq:'))



# numbers = int(input("Son kiriting : "))

# butun_son = range(2, 11)
# for butun in butun_son:
#     if numbers % butun == 0:
#         print(f'{numbers} soni {butun} ga qoldiqsiz bo`linadi')
#     elif numbers % butun != 0:
#         print(f"{numbers} son kiritmasi")
#         break