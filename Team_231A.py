n = int(input())
count = 0

for i in range(n):
	response = list( map(int, input().split() ) )

	if sum(response) > 1:
		count += 1

print(count)
