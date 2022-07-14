'''
Programa para aprovar empréstimo bancário para a compra de uma casa. Saber o valor da casa
o sálario e em quantos anos ele vai pagar. A prestação não pode exceder 30% do valor do sálario
ou então o empréstimo será negado.
'''

casa = float(input('Valoer da casa? R$'))
salario = float(input('Valor do sálario? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 0.3
print('Uma casa de R${:.2f} em {} anos terá uma prestacao de R${:.2f}.'.format(casa, anos, prestacao))
if prestacao <= minimo:
    print('Empréstimo autorizado!')
else:
    print('Empréstimo negado!')



