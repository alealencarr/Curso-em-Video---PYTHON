lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-'*30)
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista na forma decrescente fica: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print("O valor 5 não faz parte da lista!")