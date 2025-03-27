'''resp = str(input('Digite o seu sexo [M/F]:')).strip().upper()[0]
while resp != "M" and resp != "F":
    resp2 = str(input("Resposta errada! Digite o sexo com [M/F]:"))
if resp == 'M':
    print('Obrigado! Você é do sexo {}asculino.'.format(resp))
if resp == 'F':
    print("Obrigado! Você é do sexo {}eminino.".format(resp))'''

sexo = str(input("Informe seu sexo: [M/F]")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))