nome = input('Digite o seu nome:')
print(f"Boa noite {nome}")
idade = int(input(f'Digite a sua idade {nome} :'))
nascimento = 2022 - idade
print(f"{nome} sua data de nascimento é {nascimento}")
if idade >= 18:
    print(f"{nome} você já pode dirigir")
else:
    print(f"{nome} você ainda não tem idade para dirigir")