#from random import sample
#alu1 = str(input('Primeiro aluno:'))
#alu2 = str(input('Segundo aluno:'))
#alu3 = str(input('Terceiro aluno:'))
#alu4 = str(input('Quarto aluno:'))
#lista = [alu1, alu2, alu3, alu4]
#escolhido = sample(lista,4) 
#print('A ordem da apresentação será {}'.format(escolhido))
import random
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem da apresentação será:')
print(lista)