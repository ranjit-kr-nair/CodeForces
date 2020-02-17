n = int(input())

force = [0, 0, 0]

for i in range(n):
	x = list( map( int, input().split() ) )

	for j in range(3):
		force[j] += x[j]

if force[0] == force[1] == force[2] == 0:
	print("YES")
else:
	print("NO")