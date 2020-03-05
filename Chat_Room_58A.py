string = input()
hello = "hello"
typed = []

for alphabet in string:
	if alphabet in hello:
		typed.append(alphabet)

final = []
count = 0

for alphabet in typed:
	if alphabet in hello[count]:
		count += 1
		final.append(alphabet)

		if count > 4:
			break

final = "".join(final)

if final == "hello":
	print("YES")
else:
	print("NO")
