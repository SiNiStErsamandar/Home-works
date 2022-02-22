mevalar = ['olma', 'anor', 'anjir', 'shaftoli', 'banan']
# harf = 'b'
# mevalar_b = list(filter(lambda meva:meva.startswith(harf),mevalar))
# print(mevalar_b)

mevalar_a_r = list(filter(lambda meva:meva.startswith('a') and meva.endswith('r'), mevalar))

print(mevalar_a_r)