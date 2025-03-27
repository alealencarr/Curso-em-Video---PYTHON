matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = somater = maiorseg = maival = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
#RESOLUÇÃO GUANABARA SOMA TERCEIRA COLUNA
# for linha in range(0,3):
#     somater += matriz[linha][2]
for numero in matriz:
    if len(matriz) == 0:
        maiorseg = numero[1]
    else:
        if numero[1] > maiorseg:
            maiorseg = numero[1]
    somater += numero[2]
for numero in matriz[1]:
    listamaival = [numero]
    #maival = max(listamaival)
    if len(listamaival) == 0:
        maival = numero
    else:
        if numero > maival:
            maival = numero

print('=-'*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
    print()
print(f'A soma de todos os valores pares totaliza {soma}')
print(f'O maior valor da segunda coluna é {maiorseg}')
print(f'A soma da terceira coluna é {somater}')
print(f'O maior valor da segunda linha é {maival}')