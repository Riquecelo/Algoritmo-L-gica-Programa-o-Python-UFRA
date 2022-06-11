x = int(input('informe um número para iniciar:'))
y = int(input('informe um número para  finalizar: '))
lista = list(range(x, y+1))
#print(lista)
numPar = []
for i in lista:
    if(i%2 ==0):
        numPar.append(i)
print(numPar)