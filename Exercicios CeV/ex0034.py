s = float(input("Qual é o seu salário?"))
if s >= 1250.00:
    a = s*1.10
    print("Parabéns!Você recebeu um aumento de 10%")
else:
    a = s*1.15
    print("Parabéns!Você recebeu um aumento de 15%")
print("Seu novo salário é: {:.2f}.".format(a))
print('-==-'*20)


