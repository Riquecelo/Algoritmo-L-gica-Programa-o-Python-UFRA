'''--- Listas e Tuplas ---'''
'''Listas'''
nomes_paises = ['Brasil','Argentina','China','Canadá','Japão']
'''
#função len() exibe o tamanho da lista 
print('tamanho da lista:', len(nomes_paises))

#exibindo elementos pela posição
print(nomes_paises[4])

#exibindo elementos de última posição
print(nomes_paises[-1])
print(nomes_paises)
#inserindo elementos em uma posição específica
nomes_paises[4] = 'Colômbia'
print(nomes_paises)'''

'''Função Slice(fatiamento)
print(nomes_paises)
print(nomes_paises[1:3],'\n')

print(nomes_paises)
print(nomes_paises[1:-1],'\n')

print(nomes_paises)
print(nomes_paises[2:],'\n')

print(nomes_paises)
print(nomes_paises[:3],'\n')

print(nomes_paises)
print(nomes_paises[::2],'\n')

print(nomes_paises)
print(nomes_paises[::-1])'''

'''Virificação de elementos na lista'''
#exemplos
print('Brasil' in nomes_paises) #verifica se está

print('Canadá' not in nomes_paises) #verifica se não está

'''Adicionando elementos'''
lista_capitais = []

lista_capitais.append('Brasilia')
lista_capitais.append('Buenos Aires')
lista_capitais.append('Pequim')
lista_capitais.append('Bogotá')
print(lista_capitais,'\n')

lista_capitais.insert(2,'Paris')
print(lista_capitais,'\n')

'''Removendo elementos'''
lista_capitais.remove('Buenos Aires')
print(lista_capitais,'\n')

removido = lista_capitais.pop(2)
print(lista_capitais, removido,'\n')

'''Tuplas'''
#Sintaxe de declaração de tupla
nome_estados = ('Pará', 'São Paulo', 'Goiás')
print(nome_estados, type(nome_estados),'\n')

estados_norte= 'Amazonas',
print(estados_norte, type(estados_norte),'\n')