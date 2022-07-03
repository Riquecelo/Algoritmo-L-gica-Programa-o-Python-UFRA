'''Cálculo da área do circulo'''
from os import system
from math import pi

system('cls')

print('Cálculo da área do circulo')
print('Informe o diametro do circulo:')
diametro = float(input("valor: "))
raio = diametro/2
araeCirculo = pi*(raio**2)
print(f'A área do circulo é {araeCirculo:.2f}')