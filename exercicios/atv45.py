from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0, 2)
print('''Suas opçôes:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual sua jogada?'))
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO!!!")
sleep(0.5)
print('-='*17)
print('O computador jogou {}'.format(itens[maquina]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-='*17)
if maquina == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('MAQUINA VENCE')
    else:
        print('JOGADA INVALIDA!')
if maquina == 1: # computador jogou PAPEL
    if jogador == 0:
        print('MAQUINA VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
if maquina == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('MAQUINA VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA!')
