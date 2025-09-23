#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

val = float(input('Qual o preço do produto: '))
print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
pag = int(input('Qual a forma de pagamento: '))

if pag == 1 :
    desc = val * 0.10
    val_final = val - desc
    print('O valor com o desconto vai ser: R${}'.format(val_final))
elif pag == 2 :
    desc = val * 0.05
    val_final = val - desc
    print('O valor com o desconto vai ser: R${}'.format(val_final))
elif pag == 3 :
    val_final = val / 2
    print('O valor com desconto vai ser: R${} 2 vezes sem juros'.format(val_final))
elif pag == 4 :
    vez = int(input('Vai parcelar em quantas vezes? '))
    juros =  val * 1.20
    val_final = juros / vez
    print('O valor vai ser: R${} com 20% de juros ao mês'.format(val_final))
else :
    print('Opção de pagamento invalida.')
