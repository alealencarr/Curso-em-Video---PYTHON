'''lista = []
for peso in range (1,6):
    perg = float(input("{} - Digite seu peso: ".format(peso)))
    lista = lista + [perg]
print('o maior peso foi:', max(lista))
print('o menor peso foi:', min(lista))'''

maior = 0
menor = 0
for p in range (1,6):
    peso = float(input('Peso da pessoa {}: '.format(p)))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("""O maior peso lido foi {}
O menos peso lido foi {}.""".format(maior,menor))

