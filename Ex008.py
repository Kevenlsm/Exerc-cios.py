#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
tot_id = 0
velho = 0
nome_velho = ''
tot_mulher20 = 0
for i in range(1, 5):
    print('-----{} PESSOA-----'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('M/F:')).strip()
    tot_id += idade
    if i == 1 and sexo in 'Mm':
        velho = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > velho:
            velho = idade
            nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        tot_mulher20 += 1

media_id = tot_id / 4
print('A média de idade no grupo é {}'.format(media_id))
print('O homem mais velho tem {} anos e seu nome é {}'.format(velho, nome_velho))
print('No grupo exite {} mulher(es) com menos de 20 anos'.format(tot_mulher20))
