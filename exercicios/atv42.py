print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a+b > c and a+c > b and b+a > c:
    print('Os segmentos acima PODEM formar um triângulo', end=' ')
    if a == b == c:
        print('EQUILATERO!')
    elif a != b != c != a:
        print('ESCALENO!')
    else:
        print('ISOCELES!') 
else:
    print('Os segmentos acima NÂO PODEM formar um triângulo')
