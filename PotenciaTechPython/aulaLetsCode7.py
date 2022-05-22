'''--- Strings ---'''
empresa= 'Google'
print(empresa)
empresa = "Google"
print(empresa)
empresa="Let's Code"
print(empresa)
frase="O professor falou: \"amanhã terá revisão\""
print(frase)

'''Indice de uma String'''
empresa= 'Google'
print(empresa[0])
'''Usando Slice em Strings'''
print(empresa[:3])
'''Metodos Strings
método aplicado sobre o valor retornado e não perpetua sobre a string, diferente na lista que o método aplicado perpetua sobre toda a lista'''
nomes_cidades = "São paulo, Belo Horizonte, Rio de Janeiro, Brasilia"
'''Métodos Split => separa os elementos de uma string'''
nomes_cidades = nomes_cidades.split(', ')
print(nomes_cidades)

'''---- Formatações de Strings ----'''

'''strip => remove espaços excessivos das strings'''
cabecalho = '      Menu Principal      '
print(cabecalho)
print(cabecalho.strip())

nome_cidade= 'rIo De jaNeirO'

'''title => deixa a string em formato de título'''
print(nome_cidade.title(),' formatado com método title')

'''capitalize => deixa a primeira string maiúscula'''
print(nome_cidade.capitalize(),' formatado com método capitalize')

'''lower => deixa toda string em minúsculo'''
print(nome_cidade.lower(),' formatado com método lower')

'''upper => deixa toda string em maiúsculo'''
print(nome_cidade.upper(),' formatado com método upper')

'''Verificação com in'''
citado = 'professor' in frase
print('\n', citado)