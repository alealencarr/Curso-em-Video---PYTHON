n = int(input('Digite um número para calcular seu Fatorial:'))
f= 1
print("Calculando {}! =".format(n), end='')
while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else '=', end='')
    f*=n
    n -= 1
print(f)

