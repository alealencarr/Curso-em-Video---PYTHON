p1 = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Digite a razão da PA: '))
contador = 0
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while contador <= total:
        print(p1, '> ', end='')
        p1 +=rz
        contador += 1
    print('PAUSE!')
    mais = int(input('Quantos termos a mais você deseja?'))
print('Progressão finalizada com {} termos mostrados.'.format(total))

'''primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
mais = 10
while not mais == cont:
    print('{} -> '.format(primeiro), end='')
    cont += 1
    primeiro += razao
    if cont == mais:
        print('PAUSA')
        pedido = int(input('Quantos termos você quer mostrar a mais?: '))
        mais += pedido
print('Progressão finalizada com {} termos mostrados'.format(cont))'''
