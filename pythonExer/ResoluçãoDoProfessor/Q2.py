'''
Entrada: raio da base do cone, altura . raio da base do cilindro + altura
do cilindro , raio da esfera

Processamentos: calculos de cada volume

Saída: mensagem informando o valor de cada volume e qual o maior e o
menor volume
'''
from math import pi

print('Raio do cone:')
r_cone = float(input())
print('altura do cone:')
alt_cone = float(input())
v_cone = 1/3 * pi * r_cone**2 * alt_cone
print('Volume do cone = {:.2f}'.format(v_cone))

print('Raio do cilindro:')
r_cilindro = float(input())
print('Altura do cilindro:')
alt_cilindro = float(input())
v_cilindro = pi * r_cilindro**2 * alt_cilindro
print('Volume do cilindro = {:.2f}'.format(v_cilindro))

print('Raio da esfera:')
r_esfera = float(input())
v_esfera = 4/3 * pi * r_esfera**3
print('Volume da esfera = {:.2f}'.format(v_esfera))

# teste para maior volume
if v_cone > v_cilindro and v_cone > v_esfera:
    print('Cone tem o maior volume')
elif v_cilindro > v_cone and v_cilindro > v_esfera:
    print('Cilindro tem o maior volume')
else:
    print('Esfera tem o maior volume')

# teste para menor volume
if v_cone < v_cilindro and v_cone < v_esfera:
    print('Cone tem o menor volume')
elif v_cilindro < v_cone and v_cilindro < v_esfera:
    print('Cilindro tem o menor volume')
else:
    print('Esfera tem o menor volume')
