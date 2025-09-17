#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

menor = 0
maior = 0
atual = date.today().year
for i in range (1, 8):
    nasc = int(input('Digite em que ano a {}° pessoa nasceu: '.format(i)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('Tem {} pessoas maiores de idade'.format(maior))
print('Tem {} pessoas menores de idade'.format(menor))
