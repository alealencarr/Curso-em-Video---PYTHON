import datetime
yer = datetime.date.today().year
ano = int(input("Qual seu ano de nascimento?"))
a = yer - ano
if a <= 9:
    print(f'{a} anos. Categoria MIRIM.')
elif a > 9 and a <= 14:
    print(f'{a} anos. Categoria INFANTIL.')
elif a > 14 and a <= 19:
    print(f'{a} anos. CATEGORIA JUNIOR.')
elif a > 20 and a <= 25:
    print(f'{a} anos. CATEGORIA SÊNIOR.')
else:
    print(f'{a} anos. CATEGORIA MASTER.')
