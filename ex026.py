"""
vel = int(input('Qual a velocidade atual do carro? '))
if vel > 60:
    print('MULTADO! Limite máximo permitido. multa de R$ 280.00.')
else:
    print('Dirija com segurança!')
print('Tenha um bom dia!')
"""
vel = float(input('Qual a velocidade atual do carro?' ))
if vel > 80:
    print('MULTADO! Você excedeu o limite de velocidade 80Km/h.')
    multa = (vel-80) * 7
    print('Você deve pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança.')


