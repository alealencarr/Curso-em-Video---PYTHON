from random import randint
def sorteia(lst):
    for valor in range(0, 5):
        lst.append(randint(1, 10))
    print(f'Sorteando os 5 valores da lista: ',end='')
    for valor in lst:
        print(valor,end=' ')
    print('PRONTO!')


def somaPar(lst):
    soma = 0
    for valor in lst:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lst}, temos {soma}')


lista = []
sorteia(lista)
somaPar(lista)