n1 = int(input("Digite um número: "))
z = 0
for c in range (1, n1+1):
    if n1 % c == 0:
        print("\033[0;32m",end=' ')
        z = z+1
    else:
        print('\033[0;31m',end=' ')
    print(c,end='')
print('\n\033[mO número foi divisivel por {} números.'.format(z))
if z == 2:
    print("O número é PRIMO.")
else:
    print("O número não é PRIMO.")
























