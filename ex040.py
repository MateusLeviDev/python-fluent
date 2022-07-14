peso = float(input('Qual é seu peso: (Kg)'))
altura = float(input('Qual é sua altura: (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é: {:.2f}'.format(imc))
if imc <= 18.5:
    print('Abaixo do peso normal.')
elif 18.5 <= imc < 25:
    print('Peso ideal.')
elif 25<= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')

