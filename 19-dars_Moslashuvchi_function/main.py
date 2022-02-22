# def numbers(*raqamlar):
#     yigindi = 1
#     for num in raqamlar:
#         yigindi *= num
#     return yigindi

# number = numbers(1,2,3,4,5,6,)
# number2 = numbers(4,5,6,)
# number3 = numbers(1,2,5,6,)
# print(number)
# print(number2)
# print(number3)


def talabalar(ismi, familiyasi, **xokozo):
    xokozo['ismi'] = ismi
    xokozo['familiyasi'] = familiyasi
    return xokozo
laba = talabalar('samandar', 'abdumannopov', viloyat='Yangi yol', tugulgan_yili=2003)
print(laba)