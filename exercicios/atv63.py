print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
numero = int(input('Quantos termos voçê quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= numero:
    t3 = t1 + t2
    print(f'-> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim')