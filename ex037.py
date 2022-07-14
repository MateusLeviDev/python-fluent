n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota:'))
media = (n1 + n2)/2
print('O aluno tem média de {}'.format(media))
if media >= 7:
    print('Aprovado!')
elif media >= 5:
    print('Recuperação!')
else:
    print("Reprovado!")

'''
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota:'))
media = (n1 + n2)/2
print('O aluno tem média de {}'.format(media))
if 7 > media >= 5:
    print('Recuperação!') 
elif media < 5:
    print('Reprovado!')
else:
    print('Aprovado!')
'''
