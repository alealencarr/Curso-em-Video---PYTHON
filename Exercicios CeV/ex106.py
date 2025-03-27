def minisystem(ajuda=''):
    vermelho = '\033[0;31;107m'
    verde = '\033[0;32;107m'
    amarelo = '\033[0;33;107m'
    fimcor = '\033[m'
    from time import sleep
    ajuda = ''
    while ajuda != "FIM":
        print('~'*30)
        sleep(0.5)
        print(f'{amarelo}{"SISTEMA DE AJUDA PyHELP":^30}{fimcor}')
        print('~' * 30)
        sleep(0.5)
        ajuda = str(input(f"{amarelo}Função ou biblioteca > {fimcor}"))
        if ajuda == "FIM":
            sleep(0.5)
            print(f"{vermelho}ATÉ LOGO!{fimcor}")
            break
        sleep(0.5)
        print('~'*40)
        print(f'{verde}Acessando o manual do comando \"{ajuda}\"{fimcor}')
        print('~' * 40)
        sleep(0.5)
        help(ajuda)


minisystem()