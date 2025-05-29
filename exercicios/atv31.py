distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você esta prestes a a começar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    valor = distancia *0.50
else:
     valor = distancia *0.45
     print('E o preço da sua viagem custara R${}'.format(valor))