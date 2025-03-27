nome = str(input("Digite seu nome completo: ")).strip()
print("Bem vindo(a): {}".format(nome))
sep = nome.split()
pri = sep[0]
pri2 = sep[-1]
print("Primeiro nome: {}.\nUltimo nome: {}.".format(pri,pri2))

