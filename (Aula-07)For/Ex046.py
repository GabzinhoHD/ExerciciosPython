# Contagem regressiva
from time import sleep
print('CONTAGEM ANO NOVO:\n')

for cont in range(10, 0, -1):
    sleep(1)
    print(cont)

print('\033[1;31;40m\nFELIZ ANO NOVO!!!!')