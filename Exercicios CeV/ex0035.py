print("-=-"*30)
print("Analisador de Triângulos")
print("-=-"*30)
p= float(input("Primeiro segmento:"))
s= float(input("Segundo segmento:"))
t= float(input("Terceiro segmento:"))
r = p+s
z = s+t
y = t+p
if r > t and z > p and y > s:
    print("\033[1;36;107mPodem formar um triângulo!\033[m")
else:
    print("Não podem formar um triângulo!")
