n1 = float(input("Qual seu sálario: R$"))
n2 = n1 + (n1 * 15 / 100)
print('Se seu sálario era de R${:.2f}, com 15% de aumento irá passar para R${:.2f}.'.format(n1, n2))