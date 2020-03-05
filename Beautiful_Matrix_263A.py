for num in range(5):

    x = input().split()

    try:
        j = x.index("1")
        i = num
    except:
        pass

print( abs(i-2) + abs(j-2) )
