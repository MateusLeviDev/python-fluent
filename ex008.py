larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem {} de largura e {} de altura, então, possui área de {}m²'.format(larg, alt, área))
tinta = área / 2
print('Dessa maneira, a quantidade de tinta usada será de {}l'.format(tinta))