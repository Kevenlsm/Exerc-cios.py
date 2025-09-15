#um programa que leia um número inteiro e diga se ele é ou não um número primo.
n1 = int(input('Digite um número inteiro: '))
tot = 0
for i in range (1, n1 + 1):
    if n1 % i == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi divisivel {} vezes'.format(n1, tot))
if tot == 2:
    print('O número digitado é primo.')
else:
    print('O número digitado não é primo!!!')

