print('-=' * 15)
print('Analisador de Triângulos!')
print('-=' * 15)

# Entrada dos lados
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

print(f'Lados do triângulo: {r1}, {r2}, {r3}')

# Verificação se forma um triângulo
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Esse conjunto de segmentos PODE formar um triângulo.')

    # If dentro de outro if (aninhado)
    if r1 == r2 == r3:
        print('Esse é um triângulo Equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Esse é um triângulo Isósceles.')
    else:
        print('Esse é um triângulo Escaleno.')
else:
    print('Esse conjunto de segmentos NÃO pode formar um triângulo.')