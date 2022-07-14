""" Crie um programa que: Leia o nome da pessoa> Mostre em lower e upper. Quanros letras ao todo. E quantas tem o 1° """
n1 = str(input('Digite seu nome completo: ')).strip()
div = n1.split()
print(n1.lower())
print(n1.upper())
print(len(n1)-n1.count(' '))
print(len(div[0]))
# ou também: print(n1.find(' '))

