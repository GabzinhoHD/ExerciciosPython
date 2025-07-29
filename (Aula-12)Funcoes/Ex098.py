# Contador
from time import sleep
print('CONTADOR:\n')

def contador(inicio, fim, passo):
    
    print(f'Contadando de {inicio} até {fim}, de {passo} em {passo}:')

    if inicio > fim:
        passo = int('-' + str(passo)) # Se for decrescente passo fica negativo
        fim += -1 
    else:  
        fim += 1

    for i in range(inicio, fim, passo):
        print(i, end = ' ', flush = 'False')
        sleep(0.5)
    
    print('FIM.')
    print('=+' * 20)
        
print('Exemplos:')
print('=+' * 20)

contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é a sua vez:')
inicio = int(input('|Inicio: '))
fim = int(input('| Fim: '))
passo = int(input('| Passo: '))

print('=+' * 20)
contador(inicio, fim, passo)
