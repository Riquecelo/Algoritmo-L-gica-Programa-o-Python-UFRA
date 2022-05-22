'''--- Estrutura de Repetição ---

contador = 0
while contador < 10:
    contador = contador+1
    if contador == 1:
        print(contador,'loça limpa')
    else:
        print(contador,'Loças limpas')
print('Fim da execução')'''

texto = input('Digite sua senha: ')
while texto != 'letscode':
    texto = input('Senha inválida. Tente novamente: \n')
print('Acesso permitido')