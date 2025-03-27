num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))
if num1 >= num2 and num1 >= num3:
    print("O maior valor digitado foi: {}.".format(num1))
else:
    if num2 >= num1 and num2 >= num3:
        print("O maior valor digitado foi: {}.".format(num2))
    else:
        if num3 >= num2 and num3 >= num1:
            print("O maior valor digitado foi: {}.".format(num3))
if num1 <= num2 and num1 <= num3:
    print("O menor valor digitado foi: {}.".format(num1))
else:
    if num2 <= num1 and num2 <= num3:
        print("O menor valor digitado foi: {}.".format(num2))
    else:
        if num3 <= num2 and num3 <= num1:
            print("O menor valor digitado foi: {}.".format(num3))
print("-=-"*30)

