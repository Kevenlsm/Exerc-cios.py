#Mostrar seno,cosseno e tangente.
import math

ang = float(input('Digite um angulo qualquer: '))

rad = math.radians(ang)
sen = math.sin(rad)
coss = math.cos(rad)
tang = math.tan(rad)

print('O seno é {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(sen,coss,tang))