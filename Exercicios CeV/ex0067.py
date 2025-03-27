while True:
    print('-' *30)
    tabuada = int(input('Quer ver a tabuada de qual valor?'))
    print('-' *30)
    if tabuada < 0:
        print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')
        break
    else:
        for c in range (0,11):
            a = tabuada * c
            print (f'{tabuada} x {c} = {a}')

