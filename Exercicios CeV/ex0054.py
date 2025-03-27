from datetime import date
c,a,z,x = str(date.today()),(c[:4]),0,0
for ano in range (1,8):
    perg = int(input("Pessoa {}, digite seu ano de nascimento: ".format(ano)))
    if int(a) - perg >= 21:
        z = z+1
    else:
        x = x+1
print('''\033[1;32m{} pessoas já atingiram a maioridade.\033[m
\033[1;31m{} pessoas ainda não atingiram a maioridade.\033[m'''.format(z,x))