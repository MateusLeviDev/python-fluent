from math import hypot
co = float(input('Medida do cateto oposto: '))
ca = float(input('Medida cateto adjacente: '))
hi = hypot(co, ca)
print('A medida da hipotenusa é: {:.2f}'.format(hi))