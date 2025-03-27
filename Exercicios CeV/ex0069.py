conthomem = 0
somapessoas = 0
mulhermenor = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    pessoa1 = ' '
    while pessoa1 not in 'MmFf':
        pessoa1 = str(input('DIGITE SEU SEXO [M/F]: ')).strip().upper()[0]
    pessoa2 = -1
    while pessoa2 < 0:
        pessoa2 = int(input('DIGITE A SUA IDADE: '))
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Você deseja continuar? [S/N]')).strip().upper()[0]
    if pessoa2 > 18:
        somapessoas += 1
    if pessoa1 == 'M':
        conthomem +=1
    if pessoa1 == 'F' and pessoa2 < 20:
        mulhermenor +=1
    if continuar == 'N':
        break
print(f"""Total de pessoas com mais de 18 anos: {somapessoas}
Ao todo temos {conthomem} homens cadastrados
E temos {mulhermenor} com menos de 20 anos""")

