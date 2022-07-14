real = float(input('Quanto você tem na carteira? R$'))
dolar = real / 5.32
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))