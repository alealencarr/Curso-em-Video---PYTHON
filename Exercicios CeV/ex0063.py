'''
pritn('SEQUENCIA DE FIBONACCI')
numero = int(input('Digite um número:'))
anterior = 0
proximo = 1
fibonacci = 0
lista = []
while fibonacci <= numero:
    lista += [anterior, proximo]
    anterior += proximo
    proximo += anterior
    fibonacci +=1
print(lista[0:numero])'''

#guanabara
'''n = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print ('{} > {}'.format(t1,t2),end='')
cont = 3
while cont <= n:
    t3 = t1+t2
    print(' > {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' > FIM')'''


print('SEQUENCIA DE FIBONACCI')
numero = int(input('Digite um número:'))
anterior = 0
proximo = 1
print(anterior,'>', proximo,'> ' ,end='')
fibonacci = 3
while fibonacci <= numero:
    terceiro = anterior + proximo
    print(terceiro,'> ', end='')
    anterior = proximo
    proximo = terceiro
    fibonacci += 1
print('FIM!')