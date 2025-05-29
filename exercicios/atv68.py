from random import randint

print('=-' * 30)
print('VAMOS JOGAR ÍMPAR OU PAR')
print('=-' * 30)

v = 0

while True:
    jogador = int(input('Diga um valor: '))
    maq = randint(1, 10)
    total = jogador + maq
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    
    print(f'Você jogou {jogador} e o computador {maq}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!\n')
            v += 1
        else:
            print('VOCÊ PERDEU!\n')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('VOCÊ VENCEU!\n')
            v += 1
        else:
            print('VOCÊ PERDEU!\n')
            break

print(f'GAME OVER! Você venceu {v} vez(es).')
