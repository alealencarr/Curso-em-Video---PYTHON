'''print ('='*30)
print('{:^30}'.format('BANCO CEV'))
print ('='*30)
valor = int(input('Que valor você quer sacar? R$'))
cont50 = cont20 = cont10 = cont1 = 0
while True:
    if valor >= 50:
        valor -= 50
        cont50 += 1
    elif valor >= 20 and valor < 50:
        valor -= 20
        cont20 +=1
    elif valor >=10 and valor < 20:
        valor -= 10
        cont10 +=1
    elif valor >=1 and valor < 10:
        valor -= 1
        cont1 +=1
    if valor < 1:
        break
print(f"Total de {cont50} cédulas de R$50" if cont50 > 0 else '')
print(f'Total de {cont20} cédulas de R$20' if cont20 > 0 else '')
print(f'Total de {cont10} cédulas de R$10'if cont10 > 0 else '')
print(f'Total de {cont1} cédulas de R$1'if cont1 > 0 else '')'''

print ('='*30)
print('{:^30}'.format('BANCO CEV'))
print ('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >=céd:
        total -= céd
        totcéd +=1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
