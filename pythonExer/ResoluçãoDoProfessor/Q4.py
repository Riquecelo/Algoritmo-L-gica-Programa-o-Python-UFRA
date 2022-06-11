
print('a:')
a = float(input())
print('b:')
b = float(input())
print('c:')
c = float(input())
print('d:')
d = float(input())
print('e:')
e = float(input())
print('f:')
f = float(input())

x = (c*e - b*f)/(a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

print('x ={:.4f}  e y = {:.4f}'.format(x, y))
