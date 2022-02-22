def oraliq(min,max,qadam=None):
    sonlar = []
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar
print(oraliq(0,100))

