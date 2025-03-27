'''import math
co = float(input("COMPRIMENTO DO CATETO OPOSTO:"))
ca = float(input("COMPRIMENTO DO CATETO ADJACENTE:"))
hip = ca**2+co**2
rq = (math.sqrt(hip))
print ("A hipotenusa vai medir {:.2f}".format(rq))'''

import math
co = float(input("COMPRIMENTO DO CATETO OPOSTO:"))
ca = float(input("COMPRIMENTO DO CATETO ADJACENTE:"))
hi = math.hypot(co, ca)
print ("A hipotenusa vai medir {:.2f}".format(hi))


