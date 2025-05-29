print('GERADOR DE PA')
print('-='*10)

primeiro = int(input('Primeiro termo:'))
razao = int(input('Qual a razâo:'))
cont = 0
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voçê quer mostrar a mais? '))
print('FIM')
print(f'Progressão finalizada com {total} termos mostrados.')
