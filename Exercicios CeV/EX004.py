a=input("Digite algo:")
print("o tipo primitivo desse valor é",type(a))
print("Só tem espaços?{}".format(a.isspace()))
print(f'É númerico?{a.isnumeric()}')
print(f'É alfabético?{a.isalpha()}')
print(f'É alfanúmerico?{a.isalnum()}')
print(f'Está em letras maiúsculas?{a.isupper()}')
print(f'Está em letras minúsculas?{a.islower()}')
print(f'Está capitalizada?{a.istitle()}')
