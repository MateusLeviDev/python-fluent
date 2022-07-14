r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podemos formar um triângulo.')
    if r1 == r2 == r3:
        print('Forma-se TRIÂNGULO EQUILÁTERO.')
    if r1 != r2 and r2 != r3 and r3 != r1:
        print('Forma-se TRIÂNGULO ESCALENO.')
    else:
        print('Forma-se TRIÂNGULO ISÓSCELES.')
else:
    print('Os segmentos não formam triângulo.')