import datetime
anoatual = datetime.date.today().year
dicionario = {}
dicionario['Nome'] = str(input('NOME:'))
anodenascimento = int(input('Ano de Nascimento: '))
dicionario['Idade'] = anoatual - anodenascimento
dicionario['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dicionario['CTPS'] != 0:
    dicionario['Contratação'] = int(input('Ano de contratação: '))
    dicionario['Salario'] = float(input('Salário: '))
    dicionario['Aposentadoria'] = (35 - (anoatual - dicionario['Contratação'])) + dicionario['Idade']
print('-='*30)
for c,v in dicionario.items():
    print(f'   -> {c} tem o valor {v}')
