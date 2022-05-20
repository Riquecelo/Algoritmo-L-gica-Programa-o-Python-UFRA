from math import pi
print('valor de pi =',pi)
#CONE
'''
h_cone -> altura do cone
d_cone -> diâmetro da base do cone
r_cone -> raio da base do cone
volume_cone -> volume do cone
'''

print('Digite os valores do cone!')
h_cone = float(input('Digite a altura do cone:'))
d_cone = float(input('Digite o diâmetro da base do cone:'))
r_cone = d_cone/2
volume_cone = (pi * r_cone**3 *h_cone)/3
print(f'O volume do cone é {volume_cone}')
print(f'O raio do cone é {r_cone}')

#CILINDRO
'''
h_cilin -> altura do cilindro
d_cilin -> diâmetro da base do cilindro
r_cilin -> raio da base do cilindro
volume_cilin -> volume do cilindro
'''
print('Digite os valores do cilindro!')
h_cilin = float(input('Digite a altura do cilindro:'))
d_cilin = float(input('Digite o diâmetro do cilindro:'))
r_cilin = d_cilin/2
volume_cilin = pi * (r_cilin**2) * h_cilin
print(f'O volume do cilindro é {volume_cilin}')

#ESFERA
'''
d_esf -> diâmetro da base da esfera
resfn -> raio da base da esfera
volume_esf -> volume da esfera
'''
print('Digite os valores da esfera!')
d_esf = float(input('Digite o diâmetro da esfera:'))
r_esf = d_esf/2
volume_esf = (4 * pi * (r_esf**3))/3
print(f'O volume do cilindro é {volume_esf}')

maior = max(volume_cilin, volume_cone, volume_esf)
print(f'o maior valor é {maior}')
menor = min(volume_cilin, volume_cone, volume_esf)
print(f'o menor valor é {menor}')

if maior == volume_cilin:
    print('O maior volume é do cilindro')
if maior == volume_cone:
    print('O maior volume é do cone')
if maior == volume_esf:
    print('O maior volume é da esfera')

if menor == volume_cilin:
    print('O cilindro tem o menor volume')
elif menor == volume_cone:
    print('O cone tem o menor volume')
else:
    print('A esfera tem o menor volume')