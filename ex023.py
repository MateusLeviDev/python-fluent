''' Programa que leia uma frase e mostre quantas vezes aparece a letra "a", em que posição ela aparece a primeira vez e na última. '''
frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A aparece na posição {}'.format(frase.find('a')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('a')+1))
# rfind = procure a partir do right

