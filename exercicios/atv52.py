num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m{}'.format(c), end=' ')
        tot += 1
    else:
        print('\033[31m{}'.format(c), end=' ')
print('\033[m')  # Reseta a cor
print(f'\nO número {num} foi divisível {tot} vezes.')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
