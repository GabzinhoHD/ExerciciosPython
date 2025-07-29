# Calculo de area
print('ANALISE DE TERRENO:\n')

def area(largura, comprimento):
    area = largura * comprimento
    print(f'A area total é: {area:.2f} m²')

larg = float(input('Digite a largura(m) do terreno: '))
comp = float(input('Digite a largura(m) do terreno: '))

print('\nResultado:')
area(larg, comp)