s = 0
c = 0
for n in range (1,501):
  if n % 2 == 1:
      if n % 3 == 0:
          s = n+s
          c = c+1
print("Somados os {} valores, resultam em: {}.".format(c,s))