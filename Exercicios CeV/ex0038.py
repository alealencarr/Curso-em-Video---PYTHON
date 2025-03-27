n1 = int(input("Digite um número: "))
n2 = int(input("Digite mais um número: "))
if n1 > n2:
    print("O número: {} é maior.".format(n1))
elif n2 > n1:
    print("O número: {} é maior.".format(n2))
elif n2 == n1:
    print("Não existe valor maior. {} e {} são iguais!".format(n1,n2))



