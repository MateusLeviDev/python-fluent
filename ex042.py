''' PROGRAMA QUE SIMULA O JOGO JOKENPÔ'''

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 12)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!!')
sleep(1)
print('PC jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)
if pc == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('PC VENCE!')
    else:
        print('!JOGADA INVÁLIDA!')

elif pc == 1:
    if jogador == 0:
        print('PC VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('!JOGADA INVÁLIDA!')

elif pc == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('PC VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('!JOGADA INVÁLIDA!')