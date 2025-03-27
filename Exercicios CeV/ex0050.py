s = 0
for a in range (0,6):
    n1 = int(input("Digite um número: "))
    if n1 % 2 == 0:
        s = s+n1
print("A soma dos números pares é: {}.".format(s))
