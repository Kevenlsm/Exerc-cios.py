#mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

n1 = int(input('Dig2ite um numero para a sua tabuada: '))
for c in range(1, 11):
    tab = n1 * c
    print('{} x {:2} = {}'.format(n1, c, tab))
