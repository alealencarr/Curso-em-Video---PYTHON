# serial=int(input("
# Digite o serial do equipamento que será excluido: "))
# for indice in range(0, len(departamentos)):
#   if seriais[indice]==serial:
#     del departamentos[indice]
#     del equipamentos[indice]
#     del seriais[indice]
#     del valores[indice]
#     break

# for indice in range(0,len(equipamentos)):
#   print("Equipamento:.. ", (indice+1))
#   print("Nome.........: ", equipamentos[indice])
#   print("Valor........: ", valores[indice])
#   print("Serial.......: ", seriais[indice])
#   print("Departamento.: ", departamentos[indice])

inventario=[]
resposta = "S"
while resposta == "S":
  equipamento=[input("Equipamento: "),
            float(input("Valor: ")),
            int(input("Número Serial: ")),
            input("Departamento: ")]
  inventario.append(equipamento)
  resposta = input("Digite S para continuar: ").upper()

for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])

busca=input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
  if busca==elemento[0]:
    print("Valor..: ", elemento[1])
    print("Serial.:", elemento[2])

depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for elemento in inventario:
  if depreciacao==elemento[0]:
    print("Valor antigo: ", elemento[1])
    elemento[1] = elemento[1] * 0.9
    print("Novo valor: ", elemento[1])

serial=int(input("Digite o serial do equipamento que será excluído: "))
for elemento in inventario:
  if elemento[2]==serial:
    inventario.remove(elemento)

for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])