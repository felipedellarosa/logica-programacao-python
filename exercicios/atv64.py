cont = 0
soma = 0
numero = 0  

while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero != 999:
        soma += numero
        cont += 1

print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
