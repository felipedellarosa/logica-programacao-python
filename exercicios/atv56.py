#soma = 0
#maioridadehomem = 0
#nomevelho= ''
#totmulher20 = 0
#for c in range(1, 5):
#    print(f'----- {c} PESSOA -----')
#    nome = str(input('Nome: ')).strip()
#    idade = int(input('Idade: '))
#    sexo = str(input('Sexo [M/F]: ')).upper().strip()
#    soma += idade
#    if c ==1 and sexo in 'Mm':
#        maioridadehomem = idade
#        nomevelho = nome
#    if sexo in 'Mm' and idade > maioridadehomem:
#        maioridadehomem = idade
#        nomevelho = nome
#    if sexo in 'Ff' and idade < 20:
#        totmulher20 += 1
#media = soma/4
#print(f'A média de idade do grupo é de {media} anos')
#print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
#print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
soma_idades = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
mulheres_menos_20 = 0

for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    soma_idades += idade

    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome
    elif sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media_idades = soma_idades / 4
print(f'\nA média de idade do grupo é de {media_idades:.1f} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_homem_mais_velho}.')
print(f'Ao todo são {mulheres_menos_20} mulheres com menos de 20 anos.')
