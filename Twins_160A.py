n = int(input())

list_of_coins = list( map( int, input().split() ) )

sorted_list_of_coins = sorted( list_of_coins, reverse=True )

sum_total = sum( sorted_list_of_coins )

if sum_total % 2 == 0:
    half_of_total_sum = sum_total / 2
else:
    half_of_total_sum = int(sum_total / 2)

cummulative_sum_of_coins = 0

for i, coin in enumerate(sorted_list_of_coins):
    cummulative_sum_of_coins += coin
    
    if cummulative_sum_of_coins > half_of_total_sum:
        break

print(i+1)