velocidade = float(input('Em que velocidade o carro estava?'))
if velocidade > 80:
    print('MULTADO, voce ultrapassou o limite da via')
    multa = (velocidade - 80) *7
    print('Você vai pagar uma multa de R${}'.format(multa))
print('Tenha um bom dia.')