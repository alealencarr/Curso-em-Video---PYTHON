alunos = []
while True:
    informacoes = [str(input('Nome: ')), float(input('Nota 1: ')), float(input('Nota 2: '))]
    alunos.append(informacoes[:])
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('QUER CONTINUAR? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-'*30)
print(f'{"N°":<4}{"NOME":<15}{"MÉDIA":>6}')
print('--'*24)
for ind, nota in enumerate(alunos):
    media = (nota[1] + nota[2]) / 2
    print(f'{ind:<4}{nota[0]:<15}{media:>6.1f}')
while True:
    mostrarnotas = int(input('Mostrar notas de qual aluno? (999 INTERROMPE): '))
    if mostrarnotas < len(alunos):
        print(f'Notas de {alunos[mostrarnotas][0]} são {alunos[mostrarnotas][1]} e {alunos[mostrarnotas][2]}')
    else:
        print('Aluno inválido. Digite novamente.')
    if mostrarnotas == 999:
        print('FINALIZANDO...')
        break
print('<<< VOLTE SEMPRE >>>')


# ficha =list()
# while True:
#     nome = str(input('Digite um numero: '))
#     nota1 = float(input('Nota 1:  '))
#     nota2 = float(input('Nota 2:  '))
#     media= (nota1+nota2) / 2
#     ficha.append([nome,[nota1,nota2],media])
#     resp = str(input('Quer continuar?[S/N] '))
#     if resp in 'Nn' :
#         break
# print ('-='*30)
# print(f'{"No.":<4}{"NOME":<10}{MÉDIA:>8}')
# print ('-='*26)
# for i,a in enumerate(ficha):
#     print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
# while True:
#     print('-' * 35)
#     opc = int(input('Mostrar notas de qual aluno? (Digite 999 para interromper): '))
#     if opc == 999:
#         print('FINALIZANDO...')
#         break
#     if opc <= len(ficha) - 1:
#         print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
# print('<<< VOLTE SEMPRE >>>')