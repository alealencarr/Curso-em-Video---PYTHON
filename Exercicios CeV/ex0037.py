num = int(input("Digite um número: "))
base = str(input("Escolha qual base de conversão você deseja:\n1-Binário\n2-Octal\n3-Hexadecimal\n\033[1mR:"))
if base == "1":
    print ("Se transformarmos em Binário teremos {}.".format(bin(num)[2:]))
elif base == '2':
    print("Se transformarmos em Octal teremos {}.".format(oct(num)[2:]))
elif base == '3':
    print("Se transformarmos em Hexadecimal teremos {}.".format(hex(num)[2:]))
else:
    print("Opção invalida! Tente novamente.")


