soma = 0
cont = 0
for impares in range(1,501,2):
    if impares %3 ==0:
        cont = cont + 1
        soma += impares 
print('A soma de todos os {} valores é {}'.format(cont,soma))