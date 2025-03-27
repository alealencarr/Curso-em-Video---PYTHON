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
    print("\033[7;36;107mPodem formar um triângulo!\033[m")
    if p == s and s == t:
        print("Triangulo Equilátero!")
    elif p == s and p != t or t == s and t != p or p == t and p != s:
        print("Triangulo Isósceles!")
    else:
        print("Tringulo Escaleno!")
else:
    print("Não podem formar um triângulo!")

