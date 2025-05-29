print('=' * 30)
print('{:-^30}'.format('BANCO PAU MOLE'))
print('=' * 30)
saque = int(input('Que valor você quer sacar? R$'))
total = saque
cedula = 50
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'Total de {totcedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
print('=' * 30)
print('{:-^30}'.format(' VOLTE SEMPRE AO BANCO DO PAU MOLE'))
