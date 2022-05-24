'''--- Arquivos ---
# Abrindo arquivos txt com Python open/read
arquivo = open('rascunho.txt', 'r', encoding='utf-8')
texto = arquivo.read()
print(texto)
arquivo.close()

# Abrindo arquivos txt com Python open/readline com while
arquivo = open('rascunho.txt', 'r', encoding='utf-8')
linha = arquivo.readline()
while linha != '':
    print(linha, end='')
    linha = arquivo.readline()
arquivo.close()

# Abrindo arquivos txt com Python open/readline com for
arquivo = open('Links.txt', 'r', encoding='utf-8')
for linha in arquivo:
    print(linha, end='')
arquivo.close()

# Abrindo arquivos txt com Python open/read com fechamento automático
with open('links.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    print('\n')
    print(texto)'''

# Criando arquivos txt com Python
with open('texto_teste.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Essa é uma linha que escrevi usando Python\n')
    arquivo.write('Essa é a segunda linha que escrevi usando Python\n')

with open('texto_teste.txt', 'r', encoding='utf-8') as conteudo:
    print(conteudo.read(), end='')