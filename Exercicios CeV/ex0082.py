lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é ', end='')
listapar = []
for numero in lista:
    par = numero % 2
    if par == 0:
        listapar.append(numero)
print(f'{listapar}', end='')
print()
print(f'A lista de ímpares é ', end='')
listaimpar = []
for numero in lista:
    impar = numero % 2
    if impar == 1:
        listaimpar.append(numero)
print(f'{listaimpar}', end='')
print()
