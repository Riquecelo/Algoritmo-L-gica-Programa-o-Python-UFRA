"""Não existe a estrutura de repetição do tipo Case no Python
Podemos chegar em algo semelhante usando Dicionarios e Funções do Python
"""
"""Exemplo"""

def opcao1():
    print('Voce escolheu a opcao 1')

def opcao2():
    print('Voce escolheu a opcao 2')

def opcao3():
    print('Voce escolheu a opcao 3')

opcoes = {1:opcao1, 2:opcao2, 3:opcao3}

opcoes.get(2)()