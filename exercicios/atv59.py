primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
opcoes = 0
while opcoes != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    opcoes = input('Qual sua opção? ')
    if opcoes == '1':
        print(f'A soma entre {primeiro} + {segundo} é {primeiro+segundo}')
    elif opcoes == '2':
        print(f'O resultado de {primeiro} x {segundo} é {primeiro*segundo}')
    elif opcoes == '3':
        if primeiro > segundo:
            print(f'Entre {primeiro} e {segundo} o maior valor é {primeiro}')
        else:
            print(f'Entre {primeiro} e {segundo} o maior valor é {segundo}')
    elif opcoes == '4':
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif opcoes == '5':
        print("Saindo...")
    else:
        print("Opção inválida!")
