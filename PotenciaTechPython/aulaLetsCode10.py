'''--- Estrutura de repetição For ---'''
#percorrendo uma lista com for
nomes_cidades =['São Paulo', 'Londres', 'Tóquio', 'Paris']
for nome in nomes_cidades:
    print(nome)

''' se fosse feito com while
contador = 0
while contador < len(nomes_cidades):
    print(nomes_cidades[contador])
    contador = contador+1
'''
#percorrendo uma tupla com for
nomes_cidades2 =('Belém', 'Manaus', 'Rio Branco', 'Porto Velho')
for nome in nomes_cidades2:
    print(nome)

#acessando um dicionário com for
cidade = {
    'nome':'Rio de Janeiro',
    'estado':'Rio de Janeiro',
    'populacao_milhoes':12.2
} 
for chave in cidade:
    print(f'{chave} : {cidade[chave]}')

#usando for com range
for posicao in range(len(nomes_cidades)):
    nomes_cidades[posicao] = 'Rio de janeiro'
print(nomes_cidades)

#mais da função range
print(list(range(10)))
print(list(range(2,10)))
print(list(range(2,10,2)))