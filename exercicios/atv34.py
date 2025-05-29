salario = float(input('Qual seu salario? R$'))
if salario > 1250:
    salario = (salario/100)*10 + salario
    print('Seu aumento sera de {:.2f}'.format(salario))
else:
    salario = (salario/100)*15 + salario
    print('Seu aumento sera de {:.2f}'.format(salario))
