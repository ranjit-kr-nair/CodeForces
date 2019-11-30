string = input()

string = string.lower()
y = ""

for x in string:
	if x in ['a', 'e', 'i', 'o', 'u', 'y']:
		continue
	else:
		y += "."
		y += x

print(y)