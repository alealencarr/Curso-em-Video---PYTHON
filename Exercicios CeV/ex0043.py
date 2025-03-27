p = float(input("Qual é seu peso? "))
a = float(input("Qual é a sua altura? "))
imc = p/(a**2)
if imc < 18.5:
    print("Seu IMC é {:.2f}, você está abaixo do Peso!".format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f}, você está no peso ideal!'.format(imc))
elif 25 <= imc < 30:
    print("Seu IMC é {:.2f}, você está sobrepeso.".format(imc))
elif 30 <= imc < 40:
    print("Seu IMC é {:.2f}, você está com obesidade!".format(imc))
else:
    print("Seu IMC é {:.2f}, você está com Obesidade Mórbida.".format(imc))

