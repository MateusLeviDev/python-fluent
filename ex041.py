from time import sleep
print('{:=^40}'.format(' LOJAS LEVI '))
preco = float(input('Preço das compras: R$'))
print("""FORMAS DE PAGAMENTO 
[1] à vista dinheiro ou cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
opcao = int(input('Qual é a opcção: '))
print('CARREGANDO...')
sleep(2)
if opcao == 1:
    total = preco - (preco * 0.1)
elif opcao == 2:
    total = preco - (preco * 0.5)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua comra será parcela em 2x de R${:.2f}.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 0.2)
    totalparcelas = int(input('Quantas parcelas? '))
    parcela = total / totalparcelas
    print('Sua compra será parcelada em {}x de R${:.2f}.'.format(totalparcelas, parcela))
else:
    total = 0
    print('!OPÇÃO INVÁLIDA!')
print('Sua compra de R${:.2f}, vai custar R${:.2f}.'.format(preco, total))


