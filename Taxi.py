n = int( input() )
groups = list( map( int, input().split() ) )

count = 0

ones = groups.count(1)
twos = groups.count(2)
threes = groups.count(3)
fours = groups.count(4)

while ones > 0 and threes > 0:
	ones -= 1
	threes -= 1
	count += 1

while ones > 0 and twos > 0:
	ones -= 2
	twos -= 1
	count += 1

if ones % 4 == 0 and ones != 0:
	count += ones // 4
	ones = 0
elif ones % 4 != 0:
	count += ones // 4 + 1
	ones = 0

if twos != 0 and twos % 2 == 0:
	count += twos // 2
	twos = 0
elif twos % 2 != 0:
	count += twos // 2 + 1
	twos = 0

taxi = count + threes + fours

print(taxi)