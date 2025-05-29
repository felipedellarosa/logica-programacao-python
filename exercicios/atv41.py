from datetime import date

cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pretoebranco': '\033[7;30m',
    'verde': '\033[32m',
    'vermelho': '\033[31m'
}

ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
print('O atleta tem {}'.format(idade))
if idade <= 9:
    print('{}MIRIM!!!{}'.format(cores['verde'], cores['limpa']))
elif idade <= 14:
    print('{}INFANTIL!{}'.format(cores['amarelo'], cores['limpa']))
elif idade <= 19:
    print('{}JUNIOR{}'.format(cores['azul'], cores['limpa']))
elif idade <= 25:
    print('{}SÊNIOR{}'.format(cores['pretoebranco'], cores['limpa']))
else:
    print('{}MASTER{}'.format(cores['vermelho'], cores['limpa']))
