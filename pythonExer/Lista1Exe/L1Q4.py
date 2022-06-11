a = float(input('Didite o valor de \'a\': '))
b = float(input('Didite o valor de \'b\': '))
c = float(input('Didite o valor de \'c\': '))
d = float(input('Didite o valor de \'d\': '))
e = float(input('Didite o valor de \'e\': '))
f = float(input('Didite o valor de \'f\': '))

x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

print(f"O resultado equivale a:\n x = {x:.4f} \n y = {y:.4f}")
