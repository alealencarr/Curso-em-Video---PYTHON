import random
import time

fimcor = '\033[m'
preto = '\033[1;32m'
contador = 0
azul = '\033[1;34m'
nome = str(input(f'{azul}Digite seu nome: '))
print(f'Olá, {nome}! Seja bem-vindo(a) ao GAME!')
print('Neste jogo você irá jogar JOKENPÔ contra a máquina e, a cada vitória terá uma dica de como conviver bem no trânsito.')
print(f'No final responderá o questionário para mostrar o que aprendeu. Porém, para chegar ao questionário deverá vencer o computador 3 vezes. \nSerá que você conseguirá? \n{nome}, eu aposto em você!!')
print('Vamos lá!')
while True:
    lista = ["Pedra","Papel","Tesoura"]
    computador = random.randint(0,2)
    print('''Escolha uma das opções abaixo:
    [0] - Pedra.
    [1] - Papel.
    [2] - Tesoura.''')
    jogador = int(input("Digite a opção escolhida: "))
    print('\033[1;31m¬-.'*6)
    print("\033[1;31mJO\033[m")
    time.sleep(1)
    print("\033[1;31mKEN")
    time.sleep(1)
    print("\033[1;31mPÔ")
    print('\033[1;31m¬-.'*6)
    time.sleep(1)
    print("\033[1;30mO COMPUTADOR ESCOLHEU: {}.\033[m\n\033[1;97mO JOGADOR ESCOLHEU: {}\033[m".format(lista[computador],lista[jogador]))
    print('\033[1;36m¬-.'*6)
    if jogador == 0: #pedra
        if computador == 1:
            print("O COMPUTADOR GANHOU!\nNão desanime. Tente novamente.")
        elif computador == 2:
            contador += 1
            print(f"O JOGADOR GANHOU!\nParabéns. Você ganhou do computador {contador} vezes.")
            print(f'{preto}A dica da vez é: Respeite as sinalzações e sinalize corretamente. Isso é essencial.{fimcor}')
        elif computador == 0:
            print("EMPATE!\nComo empatou merece uma dica bônus: Veículos maiores cuidam dos menores.")
    if jogador == 1: #papel
        if computador == 0:
            print("O COMPUTADOR GANHOU!\nNão desanime. Tente novamente.")
        elif computador == 2:
            contador += 1
            print(f"O JOGADOR GANHOU!\nParabéns. Você ganhou do computador {contador} vezes.")
            print(f'{preto}A dica da vez é: Se beber, não dirija. (Em hipótese alguma!){fimcor}')
        elif computador == 1:
            print("EMPATE!\nComo empatou merece uma dica bônus: Não responda as provocações. Não vale a pena. Lembre-se disso no trânsito.")
    if jogador == 2: #tesoura
        if computador == 0:
            print("O COMPUTADOR GANHOU!\nNão desanime. Tente novamente.")
        elif computador == 1:
            contador += 1
            print(f"O JOGADOR GANHOU!\nParabéns. Você ganhou do computador {contador} vezes.")
            print(f'{preto}A dica da vez é: Empatia significa se colocar no lugar do outro.\nA empatia é fundamental no trânsito. Leve isto para sua vida. Se coloque no lugar do outro.{fimcor}')
        elif computador == 2:
            print("EMPATE!\nComo empatou merece uma dica bônus: A vida é seu bem mais precioso, lembre-se disso no trânsito.")
    if contador == 3:
        break
print('Parabéns! Você venceu a máquina 3 vezes. Agora é hora de provar que também é uma boa pessoa no trânsito.')
p1 = str(input("""Depois de beber podemos dirigir?
[A] - Sim, sempre que bebermos poderemos dirigir.
[B] - Depende. Se for só um pouquinho não tem problema.
[C] - NÃO! EM HIPÓTESE ALGUMA.
[D] - Sem problemas, sempre que beber vou dirigir.
Escolha sua resposta: """))
if p1 == 'C':
    print('Parabéns você acertou! Continue assim.')
else:
    print('Você errou. A resposta correta era\n[C] - NÃO! EM HIPÓTESE ALGUMA.\nJogue novamente para aprender.')
p2 = str(input("""No trânsito devemos sinalizar e respeitar as sinalizações?
[A] - Sim, isso é essencial.
[B] - Sinalização não serve pra nada.
[C] - Não, isso não é importante.
[D] - Não devemos respeitar as sinalizações.
Escolha sua resposta: """))
if p2 == 'A':
    print('Parabéns você acertou! Continue assim.')
else:
    print('Você errou. A resposta correta era\n[A] - Sim, isso é essencial.\nJogue novamente para aprender.')
p3 = str(input("""O que significa empatia? A empatia é importante?
[A] - Significa "EMPATE".
[B] - Significa que devemos nos colocar no lugar do outro. É muito importante para o trânsito e para a vida.
[C] - Não acho importante.
[D] - A empatia é importante somente para as pessoas chatas.
Escolha sua resposta: """))
if p3 == 'B':
    print('Parabéns você acertou! Continue assim.')
else:
    print('Você errou. A resposta correta era\n[B] - Significa que devemos nos colocar no lugar do outro. É muito importante para o trânsito e para a vida.\nJogue novamente para aprender.')
print('Além de vencer a maquina 3 vezes, você acertou as 3 questões!\nMEUS PARABÉNS.')

