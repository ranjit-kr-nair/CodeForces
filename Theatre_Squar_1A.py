from math import ceil
from math import modf

x , y , z = tuple( map(int, input().split()) )

b, a = modf( x / z )
d, c = modf( y / z )

p = a + ceil(b)
q = c + ceil(d)

n = int( p * q )

if n > 0:
	print(n)
else:
	print(1)