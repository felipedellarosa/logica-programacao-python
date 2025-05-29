from math import sin, cos, tan, radians
angulo = float(input('Me de o angulo:'))
seno = sin(radians(angulo))
cose = cos(radians(angulo))
tang = tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo,seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo,cose))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tang))