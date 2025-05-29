from math import factorial

print('Digite um número para')
numero = int(input('Calcular seu Fatorial: '))

resultado = factorial(numero)

print(f'{numero}! = ', end='')
c = numero
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1

print(resultado)