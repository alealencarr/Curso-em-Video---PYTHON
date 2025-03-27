lista = [[],[]]
for num in range(1,8):
    valores = int(input(f'Digite o {num}° valor: '))
    if valores % 2 == 0:
        lista[0].append(valores)
    if valores % 2 == 1:
        lista[1].append(valores)
lista[0].sort()
print('=-'*30)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {sorted(lista[1])}')





