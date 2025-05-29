num = int(input('Digite um numero inteiro: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m',
         'verde': '\033[32m'
         }
print('''escolha uma das bases para conversão:
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL''')
opcao = int(input('Qual a sua opção?'))
if opcao == 1:
    print('{}O numero {} para BINÁRIO fica {}{}'.format(
        cores['azul'], num, bin(num)[2:], cores['limpa']))
elif opcao == 2:
    print('{}O numero {} para OCTAL fica {}{}'.format(
        cores['verde'], num, oct(num)[2:], cores['limpa']))
elif opcao == 3:
    print('{}O numero {} para HEXADECIMAL fica {}{}'.format(
        cores['pretoebranco'], num, hex(num)[2:], cores['limpa']))
else:
    print('ERRO!!!')
