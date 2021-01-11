food_times = [3,1,2]
N = len(food_times)
K = int(input())

temp = 0
for i in K:
    temp += 1
    if food_times[temp%N] == 0:
        temp +=1

