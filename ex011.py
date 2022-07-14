n1 = int(input('Quantos dias alugados? '))
n2 = float(input('Quantos km rodados? '))
valor = (n1 * 60) + (n2 * 0.15)
print('O valor do aluguel é de R${:.2f}'.format(valor))
