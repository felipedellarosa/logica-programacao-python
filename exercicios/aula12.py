nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Que belo nome feminino você tem')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}'.format(nome))
