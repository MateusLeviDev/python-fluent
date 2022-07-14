salario = float(input('Qual seu sálario? '))
if salario <= 1250:
    salario = (salario * 0.15) + salario
else:
    salario = (salario * 0.10) + salario
print('Seu salário passou a ser de {}'.format(salario))