n = int( input() )

for i in range(n):
	x = input()
	l = len(x) - 2

	if l > 8:
		print( "{}{}{}".format(x[0],l,x[-1]) )
	else:
		print(x)