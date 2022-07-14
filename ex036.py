ano = int(input('Em que ano você nasceu? '))
alistamento = 2022 - ano
if alistamento == 18:
    print('Você tem 18 anos e está na hora de se alistar.')
elif alistamento < 18:
    print('Ainda faltam {} ano(s) para você se alistar.'.format(18 - alistamento))
else:
    print('Você está atrasado {} ano(s)'.format(alistamento - 18))

'''
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Alistamento!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} ano(s) para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo = idade - 18
    print('Atrasado {} ano(s)'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
'''