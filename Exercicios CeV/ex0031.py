dis = float(input("Qual a distancia em KM para o destino desejado? "))
a = dis * 0.50
b = dis * 0.45
if dis <= 200:
    print("O valor cobrado é: R${:.2f}.".format(a))
else:
    print("O valor cobrado é: R${:.2f}.".format(b))

