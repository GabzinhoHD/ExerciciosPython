#Sorteando um item
from random import choice
print('SORTEIO DE ALUNOS:\n')

aluno1 = input('Nome do 1º Aluno(a): ')
aluno2 = input('Nome do 2º aluno(a): ')
aluno3 = input('Nome do 3º aluno(a): ')
aluno4 = input('Nome do 4º aluno(a): ')
# Novamente, é triste nao poder usar FOR

turma = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(turma)

print('\nResultado')
print(f'O aluno escolhido foi: {escolhido}')