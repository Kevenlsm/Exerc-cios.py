#o jogo onde o computador vai “pensar” em um número entre 0 e 10.Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
pc = randint(0, 10)
num = int(input('Tente adivinhar o número que a máquina vai escolher de 0 à 10: '))
palpite = 0

while not pc == num:
    num = int(input('Errou o número foi {} e você escolheu {}.Tente novamente: '.format(pc, num)))
    pc = randint(0, 10)
    palpite += 1
palpite += 1
print('Parabéns! Você acertou o número foi {}'.format(pc))
print('Você levou {} palpites para vencer a maquina.'.format(palpite))