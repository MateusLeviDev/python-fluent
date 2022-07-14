''' Faça um programa para sortear o nome de 4 alunos para apagar o quadro. Lendo e selecionando o escolhido. '''
from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1 , n2, n3, n4]
escolha = choice(lista)
print('O aluno escolhido foi {}'.format(escolha))