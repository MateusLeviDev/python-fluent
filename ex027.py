num = int(input('Me diga um número qualquer: '))
result = num % 2
# o resto da divisão de qualquer número par por dois é zero, e no caso do ímpar, o resultado é igual a 1
if result == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))
