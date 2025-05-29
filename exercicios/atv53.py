frase = str(input('Digite uma frase: ')).upper().strip()
inv = frase[::-1]
print('O inverso de {} é {}'.format(frase, inv))
if frase == inv:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palindromo!')
