

nap1 = float(input('Informe sua nota do Nap1: '))
nap2 = float(input('Informe sua nota do Nap2: '))
subs = float(input('Informe sua nota da prova Substitutiva: '))
mediaNaps = (nap1 + nap2)/2
mediaSubNap1 = (nap1 + subs)/2
mediaSubNap2 = (subs + nap2)/2
if(mediaNaps >= 6 or mediaSubNap1 >=6 or mediaSubNap2 >= 6):
    print('Aluno aprovado')
else:
    print('Aluno em recuperação')