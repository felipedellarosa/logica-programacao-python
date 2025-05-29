from random import randint
maq = randint(0,5)
chute = int(input('Digite um numero de 1 a 5:'))
if maq == chute:
    print('VOCE ACERTOU!!')
else:
    print('voce errou o numero era {}'.format(maq))
