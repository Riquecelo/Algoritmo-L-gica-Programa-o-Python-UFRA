
lista = [1,2,3,9,8,7]
'''
# varrendo lista com função For
print(lista)
for e in lista:
    print(e)

# varrendo lista com função Range
for e in range(9):
    print(lista[e])

# varrendo lista com função Enumerate
for e, valor in enumerate(lista):
    print(e,'-', valor)
'''

print(len(lista))#retorna a quantidade de elementos do array
print(lista[-1])#retorna o ultimo elemento 
print(lista[-3])#ou retorna elementos de tras pra frente da lista

l = ['a','b','c','d','e','f']
print('b' in l)#retorna true se o valor está na lista
print('A' in l)#a função é case sensitive
print('A' not in l)#retorna true se o valor não esta na lista
for i in l:
    print(i, end="-") #retorna elementos em uma única linha
'''
#no for normal cada elemento é retornado em uma linha diferente
for i in l: 
    print(i)
'''