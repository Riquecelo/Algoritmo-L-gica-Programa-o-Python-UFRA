'''--- Arquivos CSV ---'''
import csv

# Criando arquivos CSV
with open('user.csv', 'w', encoding='utf-8', newline='') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['Marcelo', 'Santos', 'marcelo.@email.com', 'masculino'])

# Lendo um arquivo CSV
with open('user.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)