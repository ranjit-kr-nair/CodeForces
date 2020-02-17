n = int(input())
x = input()
y = []

for i in range(n):
	if i == 0:
		y.append(x[i])
	else:
		if x[i] != x[i-1]:
			y.append(x[i])

print(n -len(y))
