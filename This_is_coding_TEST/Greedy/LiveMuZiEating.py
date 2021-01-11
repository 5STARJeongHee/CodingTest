k = int(input())
food_times = list(map(int, input().split()))

index = 0

while k == 0:    
    if food_times[index] != 0:
        food_times[index] -= 1
        k -= 1
        
    index += 1
    index = index % len(food_times)

print(index + 1)