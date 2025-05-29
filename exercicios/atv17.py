from math import  hypot
co = float(input('Valor do cateto oposto:'))
ca = float(input('Valor do cateto adjacente:'))
hip = hypot(co,ca)
print ('O comprimento da hipotenusa é {:.2f}.'.format (hip))