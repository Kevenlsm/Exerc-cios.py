#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palíndromo!')
else:
    print('não temos um palíndromo!')

