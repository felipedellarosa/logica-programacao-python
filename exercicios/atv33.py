a = int(input('Primeiro valo: '))
b = int(input('Segundo valo: '))
c = int(input('Terceiro valo: '))
# menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor é {}'.format(menor))
# maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor é {}'.format(maior))
