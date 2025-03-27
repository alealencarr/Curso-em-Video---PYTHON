from time import sleep
def contador(inicio, fim, passo):
    print('=-'*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    if inicio > fim:
        passo = -passo
        fim -= 2
    for c in range(inicio, fim+1, passo):
        print(c, end = ' ')
        sleep(0.3)
    print('FIM!')


contador(1,10,1)
contador(10,0,2)
print('-='*30)
print('Agora é a sua vez de personalizar a contagem! ')
contador(inicio=int(input('Inicio: ')),fim=int(input('Fim: ')),passo=int(input('Passo: ')))