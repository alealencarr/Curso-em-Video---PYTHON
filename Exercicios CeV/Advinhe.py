print("BEM-VINDO!")
guess=0
while guess != 9:
    g= input("Digite um número:")
    guess = int(g)
    if guess ==9:
        print("Parabéns!")
    else:
        if guess > 9:
            print("MENOS")
        else:
            print("MAIS")
print("FIM!")
                
