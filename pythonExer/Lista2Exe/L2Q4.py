while True:
    aceitaNumero = int(input('Informe o número :'))
    if aceitaNumero > 100:
        print('Informe um número inteiro menor que 100')
    else:
        break
    
lista = list(range(aceitaNumero))
print(lista)
print(sum(lista))#função sun() soma todos os valores dentro da lista
'''
lista = list(range(aceitaNumero))
total = 0
for i in lista:
    total +=i
print(total)   
'''