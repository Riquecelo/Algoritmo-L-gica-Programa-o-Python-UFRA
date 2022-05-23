'''--- Concatenação ---'''
cumprimento = 'Ola, '
nome = 'Marcelo \n'
print(cumprimento + nome)
print(nome * 5)

nome ='Marcelo'
idade = 34
n_filhos = 3
print (nome + ' tem ' + str(idade) + ' anos e ' + str(n_filhos) + ' filhos.')

'''Método Formate'''
print('{} tem {} anos e {} filhos'.format(nome,idade,n_filhos))

preco_gasolina = 3.476
print('O preço da gasolina está em R$ {:.2f}'.format(preco_gasolina))

print(f'\n{cumprimento}{nome}, o preço da gasolina esta em {preco_gasolina}')