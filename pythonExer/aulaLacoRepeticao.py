#Laço de repetição While(enquanto)
'''
contador = 0
while contador < 10:
    contador = contador + 1
    print(f'Ola Mundo! {contador}' )

#Laço de repetiçõ For(para)
for i in range(5):
    print('Estou usando Python')
'''
#Função Range(faixa) 
faixa1 = range(5)#vai de zera a cinco
faixa2 = range(5, 10)#espaço de números determinados
#print(faixa1)
#print(faixa2)

#for i in faixa1:
#    print(i)

#Função Range com passo
#for i in range(10,20,3):
#   print(i)
'''
for i in range(1,7):
    if i==4:
        break
    print(i)
'''
for i in range(1,7):
    if i ==5:
        continue
    print(i)