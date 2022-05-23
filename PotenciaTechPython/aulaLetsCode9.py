'''--- Dicionários ---'''
dados_cidade ={
    'nome':'São Paulo',
    'estado':'São Paulo',
    'area_km':1521,
    'populacao_milhoes':12.10,
}
#print(dados_cidade)
print(type(dados_cidade))

'''adicionando elementos'''
dados_cidade['país'] = 'Brasil'
#print('\n',dados_cidade)

'''acessando elementos'''
#print(dados_cidade['nome'])

'''alterando dados'''
dados_cidade['area_km']=1500
#print(dados_cidade)

'''fazendo cópia do dicionário'''
dados_cidade2 = dados_cidade.copy()
dados_cidade2['nome']='Santos'
print(dados_cidade['nome'])
print(dados_cidade2['nome'])

'''fazendo acesso com método get'''
print(dados_cidade.get('prefeito'))
print(dados_cidade.get('estado'))

'''métodos que conversores'''

print(dados_cidade.keys(),'\n') #retorna uma lista de chaves de um dicionário
print(dados_cidade.values(),'\n') #retorna uma lista de valores de um dicionário
print(dados_cidade2.items(),'\n') #retorna uma lista de tuplas(chave,valor) de um dicionário