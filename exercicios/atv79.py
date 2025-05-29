lista = list()

while True:
    n = (int(input('Digite um valor: ')))

    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso....')
    else:
        print('Valor duplicado! Não vou adicionar...')

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar [S/N]')).strip().upper()
    if resposta == 'N':
        break
print('=-'*30)
lista.sort()
print(f'Você digitou os valores {lista}')
