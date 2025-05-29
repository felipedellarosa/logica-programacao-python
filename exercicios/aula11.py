nome = input('Digite seu nome:')
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'
         }
print('Seu nome é {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))
