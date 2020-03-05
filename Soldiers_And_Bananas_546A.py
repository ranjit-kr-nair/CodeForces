cost, money, quantity = tuple( map( int, input().split() ) )

required = cost * quantity * (quantity + 1) // 2

borrow = required - money

if borrow > 0:
	print(borrow)
else:
	print(0)
