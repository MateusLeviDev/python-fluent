""" Jogo advinhação """
from random import randint
from time import sleep
pc = randint(0, 10) # Faz o pc escolher um número inteiro entre 0 e 10
print('-=-' * 20)
print('Vou escolher um número. tente advinhar...')
print('-=-' * 20)
player = int(input('Escolha um número: '))
print('PROCESSANDO...')
sleep(3)
if player == pc:
    print('Parabéns! Você venceu')
else:
    print('Ganhei! Escolhi {} e não {}'.format(pc, player))
