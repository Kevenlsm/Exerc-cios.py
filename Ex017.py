#Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

nota1 = float(input('Digite a sua primeira nota:'))
nota2 = float(input('Digite a sua segunda nota:'))
media = (nota1 + nota2) / 2
print('Sua media final é {}'.format(media))

if media < 5 :
    print('Voce esta reprovado!')
elif media <= 6.9 :
    print('Voce esta de recuperaçao!')
elif media <= 10 :
    print('Voce esta aprovado!')
else :
    print('Media invalida')
    