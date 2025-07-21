# Media de notas
print('APROVADO OU REPROVADO?:\n')

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))

media = (nota1 + nota2) / 2

if media > 7:
    status = '\033[1;32;40mAPROVADO\033[m'

elif media >= 5 and media <= 6.9:
    status = '\033[1;33;40mRECUPERAÇÃO\033[m'

else: 
    status = '\033[1;31;40mREPROVADO\033[m'

print('\nResultado:')
print(f'MEDIA: {media} \nSTATUS: {status}')