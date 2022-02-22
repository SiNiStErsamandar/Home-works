import random as r
def oyin_men(x=10):
    print("Keling o'ylagan son topish o'ynaymiz !")
    pc = r.randint(1, x)
    men = int(input(f"1 dan {x} gacha son o'yladim. Topa olasizmi?: "))
    taxmin_men = 0
    while True:
        taxmin_men += 1
        if men > pc:
            men = int(input("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling: "))
        elif men < pc:
            men = int(input("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling: "))
        elif men == pc:
            print(f"TOPDINGIZ! {pc} sonini o'ylagan endim. {taxmin_men} ta taxmin bilan topdingiz. Tabriklayman!!!")
            break
        else:
            print("Iltimos o'yinni buzmang !")
            continue
    return taxmin_men
def oyin_pc(x=10):
    print(f"1 dan {x} gasha son o'ylang. Men topishga harakat qilaman.")
    input(f"1 dan {x} gacha son o'ylagan bosangiz istagan tugmani kiriting yozing. ")
    taxmin_pc = 0
    minimum = 1
    maximum = x
    while True:
        taxmin_pc += 1
        if minimum != maximum:
            pc = r.randint(minimum, maximum)
        else:
            pc = minimum
        javob = input(f"Siz {pc} sonini oyladingiz: togri (T),"
                      f"men o'lagan son bundan kattaroq (+), yoki kichikroq(-)???  ".lower())
        if javob == "-":
            maximum = pc - 1
        elif javob == '+':
            minimum = pc + 1
        elif javob == 't':
            print(f"Uraa!!! {taxmin_pc} ta taxmin bilan topdim")
            break
        else:
            print("Iltimos o'yinni buzmang !")
            continue
    return taxmin_pc

        

def play(x=10):
    fraza = True
    while fraza:
        taxmin_men = oyin_men(x)
        taxmin_pc = oyin_pc(x)
        if taxmin_men > taxmin_pc:
            print(f"Siz {taxmin_men} ta taxmin bilan topdingiz, men esa {taxmin_pc} ta taxmin bilan topdim. Men yutdim !!!")
        elif taxmin_men < taxmin_pc:
            print(f"Siz {taxmin_men} ta taxmin bilan topdingiz, men esa {taxmin_pc} ta taxmin bilan topdim. TABRIKLAYMAN Siz yutdingiz !!")
        else:
            print("Hisob durrang boldi !!!")
        
        restart = int(input("Yana o'ynashni hohlaysizmi ha(1) yo'q(0): "))
        if restart == 1:
            print("Unda boshladik !")
        elif restart == 0:
            print("Maroqli o'yin uchun raxmat sog boling!")
            fraza = False
        else:
            print("Savolga javob bermadingiz !")
            continue

play()