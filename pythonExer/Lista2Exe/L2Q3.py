while True:
    nfat = int(input("Digite o número :"))
    if nfat <= 1:
        print('Só aceita numeros inteiros maires que 1')
    else:
        break

x = 1
for i in range(1,nfat):
    x = x*(i+1)
    print(x, i)
print(x)