vel = float(input("Quantos KM/h o carro está? "))
mul = (vel - 80) * 7
if vel <= 80:
    print("Você está dentro da velocidade permitida!")
else:
    print("LIMITE DE 80KM/H ULTRAPASSADO! VOCÊ FOI MULTADO. O VALOR DA MULTA É: R${:.2f}.".format(float(mul)))

