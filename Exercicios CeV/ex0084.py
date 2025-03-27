principal = []
temporaria = []
maiorpeso = menorpeso = 0
while True:
    temporaria.append(str(input('Digite seu nome: ')))
    temporaria.append(float(input('Digite seu peso: ')))
    if len(principal) == 0:
        maiorpeso = temporaria[1]
        menorpeso = temporaria[1]
    else:
        if temporaria[1] > maiorpeso:
            maiorpeso = temporaria[1]
        if temporaria[1] < menorpeso:
            menorpeso = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Ao todo, você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maiorpeso}KG. Peso de ',end='')
for p in principal:
    if p[1] == maiorpeso:
        print(f'{p[0]}... ',end='')
print()
print(f'O menor peso foi de {menorpeso}KG. Peso de ',end='')
for p in principal:
    if p[1] == menorpeso:
        print(f'{p[0]}... ',end='')
print()
