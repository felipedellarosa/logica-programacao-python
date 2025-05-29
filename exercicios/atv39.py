from datetime import date
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m',
         'verde': '\033[32m',
         'vermelho': '\033[31m'
         }
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print('{}Quem nasceu em {} tem {} anos em {}{}.'.format(
    cores['verde'], ano, idade, date.today().year, cores['limpa']))
if idade >= 18:
    print('{}Você ja se ALISTOU!{}'.format(cores['vermelho'], cores['limpa']))
elif idade < 18:
    print('{}Ainda faltam {} anos para se ALISTAR!!{}'.format(
        cores['verde'], 18 - idade, cores['limpa']))
    print('{}Seu ALISTAMENTO sera em {}{}'.format(
        cores['verde'], ano + 18, cores['limpa']))
