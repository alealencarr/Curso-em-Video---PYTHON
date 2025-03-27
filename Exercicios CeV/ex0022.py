nome = str(input("Digite seu nome completo: ")).strip()
print("Seu nome em maiusculo é: {}.".format(nome.upper()))
print("Seu nome em minusculo é: {}.".format(nome.lower()))
print("Seu nome tem {} letras.".format(len(nome) - nome.count (" ")))
div = nome.split()
print("Seu primeiro nome tem {} letras.".format(len(div[0])))


