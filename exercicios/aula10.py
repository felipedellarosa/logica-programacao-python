n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1+n2)/2
print('Sua media é {:.1f}'.format(media))
if media >=7:
    print('voce esta na media, parabens')
else:
    print('REPROVADO!')