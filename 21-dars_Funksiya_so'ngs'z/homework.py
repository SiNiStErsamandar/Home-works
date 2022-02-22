mevalar = ['olma', 'anor', 'anjir', 'shaftoli', 'banan']
harf = 'b'
mevalar_b = list(filter(lambda meva:meva.startwith(harf),mevalar))
print(mevalar_b)