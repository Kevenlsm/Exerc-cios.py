#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

nome = input('Digite seu nome: ')
alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (alt * alt)
print('Este é o seu IMC: {}'.format(imc))

if imc <= 18.5 :
    print('Seu IMC esta abaixo do peso.')
elif imc <= 25 :
    print('Seu IMC esta no peso ideal.')
elif imc <= 30 :
    print('Seu IMC esta no sobrepeso.')
elif imc <= 40 :
    print('Seu IMC esta em obesidade.')
else :
    print('Seu IMC esta em obesidade morbida.')
