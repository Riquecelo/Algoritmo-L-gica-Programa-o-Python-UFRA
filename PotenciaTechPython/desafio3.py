nome_cidade = input('Que cidade do Brasil é conhecida como cidade maravilhosa? ')
nome_cidade = nome_cidade.strip()
while nome_cidade.lower() != 'rio de janeiro':
    print('tente novamente!')
    nome_cidade = input('Que cidade do Brasil é conhecida como cidade maravilhosa? ')

print('Parabéns você acertou!')