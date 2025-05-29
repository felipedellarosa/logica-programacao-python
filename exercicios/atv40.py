cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m',
         'verde': '\033[32m',
         'vermelho': '\033[31m'
         }
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(
    nota1, nota2, media))
if media < 5:
    print('{}REPROVADO!!!{}'.format(cores['vermelho'], cores['limpa']))
elif 5 <= media <= 6.9:
    print('{}RECUPERAÇÂO!!!{}'.format(cores['vermelho'], cores['limpa']))
else:
    print('{}APROVADO!!!{}'.format(cores['verde'], cores['limpa']))
