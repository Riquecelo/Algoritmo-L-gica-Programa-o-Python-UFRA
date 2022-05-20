#Calculo da área do circulo
from cmath import pi

print('Descubra qual é a área do circulo.')
diametro = float(input('Informe o diâmetro do circulo:'))
raio = diametro/2
calAreaCirculo = pi * (raio**2)
print(f'O valor da área do circulo é {calAreaCirculo}')