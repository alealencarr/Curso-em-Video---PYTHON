frase = str(input("Digite uma frase: ")).strip()
fra = frase.upper()
print("A frase é: {}.".format(fra))
a = fra.count ('A')
pos = fra.find('A')
pos2 = fra.rfind('A')
print("Ela tem {} letras: 'A'.\nO primeiro está na posição {}.\nE o último {}.".format(a,pos,pos2))


