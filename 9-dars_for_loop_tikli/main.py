insonlar = []
soni = input("Bugun nechta inson bilan tanishdingiz ?: ")
jami = len(soni)
for ismlar in range(jami):
    insonlar.append(input(f'{ismlar+1}-insonning ismi : '))
print(f'Siz bugun tanishgan insonlaringiz {insonlar}')