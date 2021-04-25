from math import hypot
ca = float(input('Qual é o cateto adjacente?'))
co = float(input('Qual é o cateto oposto ?'))
hi = hypot(co, ca)
print('a hipotenusa vai medir {:.2f}'.format (hi))
