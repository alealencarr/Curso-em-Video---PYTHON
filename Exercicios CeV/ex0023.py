n = int(input("Digite um número entre 0 e 9999: "))
u= n // 1 % 10
d= n // 10 % 10
c= n // 100 % 10
m= n // 1000 % 10
print("Unidade: {}.".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))

#n = input ("Escreva um numero de 0 até 9999: ")
#v = ("{:>4}".format(n))
#print("Unidade {}\nDezena {}\nCentena {}\nMilhar {}.".format(v[3],v[2],v[1],v[0]))


