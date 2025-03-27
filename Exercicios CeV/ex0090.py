dicionario = {}
dicionario['Nome'] = str(input('NOME:'))
dicionario['Média'] = float (input(f'Média de {dicionario["Nome"]}: '))
if dicionario["Média"] >= 7:
    dicionario['Situação'] = 'Aprovado'
elif dicionario["Média"] >= 5 and dicionario['Média'] < 7:
    dicionario['Situação'] = 'Recuperação'
else:
    dicionario['Situação'] ='Reprovado'
for k,v in dicionario.items():
    print(f'{k} é igual a {v}')
