s = float(input('Qual a distância total da viagem? '))
print('Você está preste a começar uma viagem de {}Km'.format(s))
if s <= 200:
    valor = s * 0.50
else:
    valor = s * 0.45
print('O valor de sua passagem será de R${:.2f}'.format(valor))

'''
valor = s * 0.50 if s <= 200 else s * 0.45
'''
