p1 = int(input("Digite o primeiro termo da PA: "))
rz = int(input("Qual é a razão dessa PA?\nR:"))
dez = p1 + (10-1) * rz
for c in range (p1,dez+rz,rz):
    print(c, end=' ')


