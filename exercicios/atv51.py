print('='*10)
print('10 TERMOS DE UMA PA')
print('='*10)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Qual a razâo:'))
decimo = primeiro + (10-1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end='-')
print('ACABOU')