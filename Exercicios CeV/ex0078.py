lista = []
maior = 0
menor = 0
for numero in range (0,5):
    lista.append(int(input(f'Digite o {numero+1}° valor: ')))
    if numero == 0:
        maior = lista[numero]
        menor = lista[numero]
    else:
        if lista[numero] > maior:
            maior = lista[numero]
        if lista[numero] < menor:
            menor = lista[numero]
print('=-'*30)
print(f'Você digitou os valores {lista}')
print(f'O maior número digitado foi {maior} e a(s) sua(s) posição(ões): ', end='')
for pos, valor in enumerate(lista):
    if valor == maior:
        print(f'{pos+1}... ', end='')
print()
print(f'O menor número digitado foi {menor} e a( s) sua(s) posição(ões): ', end='')
for pos, valor in enumerate(lista):
    if valor == menor:
        print(f'{pos+1}... ',end='')
print()