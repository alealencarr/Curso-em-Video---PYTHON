lista = []
soma = 0
while True:
    dicionario = {'nome':str(input('Digite seu nome: '))}
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
    dicionario['sexo'] = sexo
    dicionario['idade'] = int(input('Digite sua idade: '))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    lista.append(dicionario.copy())
    if continuar == 'N':
        break
print('-='*30)
print(f'- O grupo tem {len(lista)} pessoas.')
for idade in lista:
    soma += idade['idade']
    média = soma / len(lista)
print(f'- A média de idade é de {média:.2f} anos.')
m = []
for mul in lista:
    if mul['sexo'] == 'F':
        m.append(mul['sexo'])
print(f'- As mulheres cadastradas foram: ',end='')
for mulher in lista:
    if mulher['sexo'] == 'F':
        print(f'{mulher["nome"]}..',end='')
    elif len(m) == 0:
        print('Não foram cadastradas mulheres.',end='')
        break
print(f'\n- Lista das pessoas que estão acima da média:')
a = []
for idad in lista:
    if idad['idade'] > média:
        a.append(idad['idade'])
for pessoa in lista:
    if pessoa['idade'] > média:
        print(f'    -> {pessoa}')
    elif len(a) == 0:
        print('     -> Não temos pessoas com idade acima da média.')
        break
print()
print('<< ENCERRADO >>')
