x = input()
n = len(x)

count = 1

for i in range(n-1):
	if x[i] == x[i+1]:
		count += 1

		if count > 6:
			break

	else:
		count = 1

if count > 6:
	print("YES")
else:
	print("NO")
