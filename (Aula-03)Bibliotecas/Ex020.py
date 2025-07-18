#Sorteando um ordem
from random import shuffle
print('SORTEIO DE ORDEM DOS ALUNOS:\n')

aluno1 = input('Nome do 1º Aluno(a): ')
aluno2 = input('Nome do 2º aluno(a): ')
aluno3 = input('Nome do 3º aluno(a): ')
aluno4 = input('Nome do 4º aluno(a): ')

turma = [aluno1, aluno2, aluno3, aluno4]
shuffle(turma) # Embaralha a ordem da lista

print('\nResultado:')
print(f'Ordem dos alunos: {turma}') # O print é meio feio :(. Usando FOR dava pra deixar bonitinho