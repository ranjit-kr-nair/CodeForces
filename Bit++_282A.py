n = int(input())
count = 0

for i in range(n):

	x = input()

	if x[0] == "+" or x[-1] == "+":
		count += 1
	else:
		count -= 1

print(count)
