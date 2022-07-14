''' Faça um programa para sortear a sequência de nomes de 4 alunos para apresentar um trabalho. '''
from random import choice, shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1 , n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será {}.'.format(lista))
# shuffle embaralha 