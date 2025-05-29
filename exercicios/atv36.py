print('=-'*20)
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual seu salario? R$'))
anos = int(input('Em Quantos anos vai pagar?'))
print('=-'*20)
prestacao = casa/(anos*12)
limite = salario*0.3
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de {:.2f} '.format(
    casa, anos, prestacao))
if prestacao <= limite:
    print('Emprestimo pode ser concedido')
else:
    print('Emprestimo negado')
