print('-'*30)
print('      LOJA SUPER BARATÃO')
print('-'*30)

total = cont = 0
menor_preco = 0
produto_mais_barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco

    if preco > 1000:
        cont += 1

    # Inicializa ou atualiza o produto mais barato
    if total == preco or preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = produto

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi "{produto_mais_barato}" que custa R${menor_preco:.2f}')
