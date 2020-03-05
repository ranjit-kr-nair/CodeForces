x = input()

x = x.split("+")

x.sort()

y = "".join([ var + "+" for var in x ])

print(y[:-1])
