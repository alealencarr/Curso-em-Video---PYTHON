from time import sleep
def maior(*num):
    print('=-'*25)
    print('Analisando os valores passados...')
    maior_valor = 0
    for valor in num:
        if len(num) == 0:
            maior_valor = valor
        else:
            if valor > maior_valor:
                maior_valor = valor
    for valor in num:
        print(valor,end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor informado foi o {maior_valor}')
    sleep(0.5)


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(2,1)
maior(6)
maior()

