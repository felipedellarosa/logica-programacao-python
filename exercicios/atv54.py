from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c} pessoa nasceu? '))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} maiores de idade')
print(f'Ao todo tivemos {totmenor} menores de idade')
