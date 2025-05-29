print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a+b > c and a+c > b or b+a > c:
    print('Os segmentos acima PODEM formar um triângulo')
else:
    print('Os segmentos acima NÂO PODEM formar um triângulo')
