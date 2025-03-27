import random
computador = random.randint(0,5)
print ("-=-"*20)
print ("Vou pensar em um número de 0 a 5. Tente adivinhar...")
print ("-=-"*20)
jogador = int(input("Em que número eu pensei? "))
print("Processando...")
if jogador == computador:
    print ("Parabéns. Você ganhou!")
else:
    print ("GANHEI! Eu pensei no número {}. Não no número {}.".format(computador,jogador))
print("FIM DE JOGO!")
