x = int( input() )

lucky = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

check = 0

for num in lucky:
	if x % num == 0:
		print("YES")
		check += 1
		break

if check == 0:
	print("NO")