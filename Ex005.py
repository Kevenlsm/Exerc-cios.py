#Crie um programa que faça o computador jogar Jokenpô com você

from random import randint
from time import sleep

pc = randint(0,2)
itens = ('papel', 'pedra', 'tesoura')
print('[0] para Papel.')
print('[1] para pedra.')
print('[2] para tesoura.')
mao = int(input('Jogue sua mão: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')

print('=+=' * 10)
print('O computador escolheu: {}'.format(itens[pc]))
print('O jogador escolheu: {}'.format(itens[mao]))
print('=+=' * 10)

if pc == 0 :
    if mao == 0 :
        print('Ambos jogaram papel,EMPATOU.')
    elif mao == 1 :
        print('Voce perdeu')
    elif mao == 2 :
        print('Voce ganhou')
elif pc == 1 :
    if mao == 0 :
        print('Voce ganhou')
    elif mao == 1 :
        print('Ambos jogaram Pedra,EMPATOU.')
    elif mao == 2 :
        print('Voce perdeu')
elif pc == 2 :
    if mao == 0 :
        print('Voce perdeu')
    elif mao == 1 :
        print('Voce ganhou')
    elif mao == 2 :
        print('Ambos jogaram tesoura,EMPATOU.')
