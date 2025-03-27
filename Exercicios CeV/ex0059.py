a,b = int(input('Digite um valor: ')), int(input("Digite outro valor: "))
usuario = 0
while usuario != 5:
    print ("""MENU DE OPÇÕES:
    [1] - SOMAR
    [2] - MULTIPLICAR
    [3] - MAIOR
    [4] - NOVOS NÚMEROS
    [5] - SAIR DO PROGRAMA.""")
    usuario = int(input('Digite o número da opção desejada: '))
    if usuario == 1:
        print ('Somados os números {} e {}, resultam em {}.'.format(a,b,a+b))
    elif usuario == 2:
        print('Multiplicados os números {} e {}, resultam em {}.'.format(a, b, a * b))
    elif usuario == 3:
        if a > b:
            print("Entre os números {} e {}, o maior é {}.".format(a,b,a))
        else:
            print("Entre os números {} e {}, o maior é {}.".format(a, b, b))
    elif usuario == 4:
        print("Digite os novos valores...")
        a,b = int(input("Digite um valor:")), int(input('Digite outro valor:'))
    elif usuario == 5:
        print('Finalizando o programa...')
    else:
        print("Opção invalida, digite novamente. ")