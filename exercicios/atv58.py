from random import randint
maq = randint(1,10)
print('Sou seu computador...')
print('Acabei de pensar em um numero de 1 a 10. ')
print('Será que você conseuge advinhar qual foi? ')
tentativas = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    tentativas += 1
    if jogador > maq:
        print('Menos... Tente mais uma vez.')
    elif jogador < maq:
        print('Mais... Tente mais uma vez.')
    else:
        acertou = True
        print(f'Acertou com {tentativas} tentativa(s)! Parabéns!')