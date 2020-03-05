n, k = tuple(map(int, input().split()))
count = 0

x = list(map(int, input().split()))

for i in range(n):

	if x[i] > 0:
		if i < k:
			count += 1
		else:
			if x[i] == x[k-1]:
				count += 1

print(count)
