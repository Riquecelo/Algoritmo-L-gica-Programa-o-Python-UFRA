# Principais Métodos para manipular Listas

nomes = ['Ana','Maria', 'Pedro']
print(nomes)

#Adicionar um elemento na lista
nomes.append('Marcelo')#o novo elemento adicionado será o último da lista
print(nomes)

#Removendo elementos da lista
#----POP remove o último elemento----#
nomes.pop()#pop sem indice remove o ultimo valor da lista
print(nomes)
nomes.pop(1)#remove o valor do indice especficado
print(nomes)

#----REMOVE apaga a primeira ocorrência na lista
frutas = ['pera','maçã','banana','laranja']
print(frutas)
frutas.remove('pera')
frutas.remove('laranja')
print(frutas)

# Inserindo elemento em determinada posição
''' Sintaxe
*nome-da-lita.insert(índice,valor)
'''
frutas.insert(1,'caju')
print(frutas)

#---Contador de elementos repetidos na lista
numeros = [2,3,12,3,11,3,8,3]
rep = numeros.count(3)
print(f"a occorrência do 3 na lista é: {rep} vezes")

#----Descobrindo o indice de um valor
posisao=numeros.index(3)
print(f"o index de 3 é: {posisao}")

#----Juntando Listas----#
''' Sintaxe
*nome-da-lista.extend(nome-da-outra-lista)
'''
frutas.extend(numeros)
print(frutas)

#---Invertendo a ordem de uma lista---#
frutas.reverse()
print(frutas)

#---Ordenando uma lista---#
numeros.sort()
print(numeros)