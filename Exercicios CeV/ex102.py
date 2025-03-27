def fatorial(n, show=False):
    vallogico = 1
    for numero in range(n,0,-1):
        if show:
            print(numero,end='')
            if numero > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        vallogico *= numero
    return vallogico


print('-'*40)
print(fatorial(7,True))