'''--- Estruturas Sequenciais ---'''

'''entrada de dados
função input() toda entrada é convertida para string

idade = input('Informe sua idade: ')
print(type(idade))
idade = int(idade) #convertendo string para int
print(idade)
print(type(idade))
print('\n')'''

'''conversões dos tipos de dados
print(float('112')) #inteiro => ponto flutuante(decimal)
print(str(123.45)) #numero => string
print(bool('')) #string => booleano, saída false  
print(bool('abc')) #string => booleano, saída true
print(bool(0)) #numero => booleano, saída false
print(bool(123)) #numeero => booleano, saída true'''

'''Exemplo prático'''
salario_mensal = int(input('Digite o valor do seu salário:'))
gastos_mensal  = int(input('Digite o valor do seus gastos mensais:'))
salario_total = salario_mensal*12
gasto_total = gastos_mensal*12

montante_economizado = salario_total - gasto_total
print('O total economizado anualmente é de: ', montante_economizado)