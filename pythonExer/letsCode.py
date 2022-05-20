'''
salario_mensal = input('Qual é o seu saláro:')
salario_mensal = float(salario_mensal)

gasto_mensal = input('Qual é o seu gasto mensal:')
gasto_mensal = float(gasto_mensal)

salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12

montante_economizado = salario_total - gasto_total

print('O montante que você pode economizar anualmente é de :' ,montante_economizado)
'''
'''
passagem = 4

corrida = input('Qual o valor da corrida? :')
corrida = float(corrida)
if(corrida <= passagem):
    print('Aceitar a corrida!')
elif (corrida > passagem) and (corrida < 10):
    print('espere um pouco')
else:
    print('pegue um ônibus')
'''
'''
contador = 0
while contador < 10:
    contador = contador+1
    if contador % 2 == 0:
        print(contador, "item limpo")
    else:
        print(contador, "item sujo")
print("Fim da repetção do bloco while")
'''

'''
texto = input("Digite sua senha:")

while texto != 'Letscode':
    texto = input("Senha invália, Tente novamente:")
print('Acesso permitido')
'''
nomes_paises = ['brasil','Argentina','China','Canadá','Japão']
#print(nomes_paises)
print('tamanho da lista é:', len(nomes_paises))

print('País é:', nomes_paises[3])

print('País é:', nomes_paises[-1])

nomes_paises[4] = 'Colômbia'
print(nomes_paises[4])
print(nomes_paises)