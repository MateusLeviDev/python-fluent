nome = str(input('Digite seu nome: ')).strip()
div = nome.split()
print('Seu primeiro nome é {}'.format(div[0]))
print('Seu último nome é {}'.format(div[len(div)-1]))
# -1 pq por exemplo: Mateus Levi Souza. Tem 3 posições, então coloamos 1 a menos.
