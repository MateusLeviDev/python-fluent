from time import sleep
print('-=-' * 20)
print('Analisando triângulos')
print('-=-' * 20)
r1 = float(input('Primieiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
print('PROCESSANDO...')
sleep(3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar triângulo.')
else:
    print('Não forma triângulo.')
