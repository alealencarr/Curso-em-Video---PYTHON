'''import math
ang = float (input("Digite o Angulo que você deseja: "))
sen = (math.sin(ang))
cos = (math.cos(ang))
tang = (math.tan(ang))
print ("O ângulo de {} tem o SENO de {}.\nO ângulo de {} tem o COSSENO de {}.\nO ângulo de {} tem a TANGENTE de {}.".format(ang,sen,ang,cos,ang,tang))'''

import math
ang = float (input("Digite o Angulo que você deseja: "))
grau = math.radians(ang)
sen = (math.sin(grau))
cos = (math.cos(grau))
tang = (math.tan(grau))
print ("O ângulo de {} tem o SENO de {:.2f}.\nO ângulo de {} tem o COSSENO de {:.2f}.\nO ângulo de {} tem a TANGENTE de {:.2f}.".format(ang,sen,ang,cos,ang,tang))
