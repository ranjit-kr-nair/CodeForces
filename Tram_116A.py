n = int( input() )

crowd = 0

crowd_snap = []

for i in range(n):
	exit, enter = tuple( map( int, input().split() ) )

	crowd -= exit
	crowd += enter

	crowd_snap.append(crowd)

print(max(crowd_snap))
