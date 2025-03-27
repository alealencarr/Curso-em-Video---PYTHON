import random
n1= input("Primeiro:")
n2= input("Segundo:")
n3= input("Terceiro:")
n4= input("Quarto:")
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print("A ordem de apresentação será:\n {}".format(lista))
