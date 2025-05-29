print('=====LOJA PICA GORDA=====')
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro
[2] à vista cartâo
[3] 2X no cartâo
[4] 3X ou mais no cartâo
''')
opcao = int(input('Qual é a opçâo? '))
if opcao == 1:
    print('Sua compra de R${:.2f} vai custa R${:.2f} no final.'.format(
        preco, preco-(preco*0.1)))
elif opcao == 2:
    print('Sua compra de R${:.2f} vai custa R${:.2f} no final.'.format(
        preco, preco-(preco*0.05)))
elif opcao == 3:
    print('Sua compra de R${:.2f} vai ser parcelada em duas vezes de R${:.2f}.'. format(
        preco, preco/2))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra sera parcelada em {}x de R${:.2f} com JUROS'.format(
        parcelas, preco/parcelas))
    print('Sua compra de R${:.2f} vai custa R${:.2f} no final.'.format(
        preco, (preco*0.2)+preco))
else:
    print('\033[31mOPÇÂO INVALIDA DE PAGAMENTO!!\033[m')
