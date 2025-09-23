#Crie um programa que leia dois valores e mostre um menu na tela:[ 1 ] somar [ 2 ] multiplicar
#[ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

x = 0
n1 = float(input('Digite o Primeiro Valor: '))
n2 = float(input('Digite o Segundo Valor: '))
while not x == 5:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do Programa')
    x = int(input('Qual é a sua opção: '))
    if x == 1:
        soma = n1 + n2
        print('A soma dos números é: {}'.format(soma))
    elif x == 2:
        mult = n1 * n2
        print('A multiplicação dos números é: {}'.format(mult))
    elif x == 3:
        if n1 > n2:
            maior = n1
            print('O maior número é o {}'.format(n1))
        else:
            maior = n2
            print('O maior número é o {}'.format(n2))
    elif x == 4:
        n1 = float(input('Digite o Primeiro Valor: '))
        n2 = float(input('Digite o Segundo Valor: '))
    if x not in (1, 2, 3, 4, 5):
        print('Opção invalida.Tente novamente: ')
print('Fim do Programa volte sempre!')
