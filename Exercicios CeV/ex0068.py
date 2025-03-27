from random import randint
print('=-'*40)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*40)
contador = 0
while True:
    computador = randint(0, 10)
    jogador = int(input("Diga um valor: "))
    a = computador + jogador
    p_ou_i = ' '
    while p_ou_i not in 'PI':
        p_ou_i = str(input('Par ou ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total deu {jogador+computador}','DEU ÍMPAR' if a%2 == 1 else 'DEU PAR')
    if p_ou_i == 'I' and a%2 == 1:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        contador +=1
    elif p_ou_i == 'P' and a%2 == 0:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        contador += 1
    else:
        print('Você PERDEU!')
        print('=-' * 30)
        break
print(f'GAME OVER! Você venceu {contador}','vez' if contador <=1 else 'vezes')
