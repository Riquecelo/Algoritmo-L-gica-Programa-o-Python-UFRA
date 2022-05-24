'''--- Funções ---'''
def hello():
    print('Olá, Mundo!')
hello()

def calcula_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media
print(calcula_media(5,8,8))

#função padrão end
print('Hello,', end=' ')
print('Word')

#usando *args
def calcula_media2(*args):
    #print(args, type(args))
    soma = sum(args)
    media = soma / len(args)
    return media
print(calcula_media2(5, 9, 8))

#usando **kwargs
def print_info(**kwargs):
    print(kwargs, type(kwargs))

print(print_info(nome='Marcelo',idade=34))