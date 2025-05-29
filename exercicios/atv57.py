sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()
while sexo not in ['F', 'M']:
    print('Dados inválidos. Por favor, informe seu sexo corretamente.')
    sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()
    if sexo == 'M':
        print('Sexo M registrado com sucesso')
    elif sexo == 'F':
        print('Sexo F registrado com sucesso')
