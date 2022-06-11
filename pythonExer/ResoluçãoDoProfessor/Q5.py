from math import pi


diametro = float(input('Diametro do circulo:'))

raio = diametro/2

area = pi*raio**2

print('Area do circulo = {:.2f}'.format(area))
