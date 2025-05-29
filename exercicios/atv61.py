print('GERADOR DE PA')
print('-='*10)

primeiro = int(input('Primeiro termo:'))
razao = int(input('Qual a razâo:'))
cont = 0
termo = primeiro 

while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('ACABOU')
