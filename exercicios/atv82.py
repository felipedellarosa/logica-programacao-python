lista = list()
impares = list()
pares = list()

while True:
    num = (int(input('Digite um número: ')))
    lista.append(num)
    if num % 2 ==0:
        pares.append(num)
    else:
        impares.append(num)

    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')

