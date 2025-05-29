cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m',
         'verde': '\033[32m',
         'vermelho': '\033[31m'
         }
try:
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))

    if num1 > num2:
        print('{}O PRIMEIRO valor é maior{}'.format(
            cores['verde'], cores['limpa']))
    elif num2 > num1:
        print('{}O SEGUNDO valor é maior{}'.format(
            cores['verde'], cores['limpa']))
    else:
        print('{}Os dois valores são IGUAIS{}'.format(
            cores['verde'], cores['limpa']))
except ValueError:
    print('{}ERRO! Você precisa digitar apenas números inteiros.{}'.format(
        cores['vermelho'], cores['limpa']))
