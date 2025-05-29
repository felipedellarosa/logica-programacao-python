resp = 'S'
cont = media = soma = maior = menor = 0
while resp in 'S':
    numero = int(input('Digite um numero:'))
    cont += 1
    soma += numero
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    
media = soma / cont
print(f'\nVocê digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')