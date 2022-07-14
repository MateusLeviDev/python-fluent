''' Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. '''
from math import sin, cos, tan, radians
ang = float(input('Digite o angulo que você deseja: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('sen de {} é {:.2f} \ncos de {} é {:.2f} \ntan de {} é {:.2f}'.format(ang, sen, ang, cos, ang, tan))
