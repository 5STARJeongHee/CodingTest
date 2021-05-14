def insert_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j-1] < arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                pass

def selection_sort(arr):
    
    for i in range(len(arr)):
        max_idx = i
        for j in range(i+1,len(arr)):
            if arr[max_idx] < arr[j]:
                max_idx = j
        arr[i],arr[max_idx] = arr[max_idx], arr[i]

def count_sort(arr):
    mi = min(arr)
    ma = max(arr)
    carr = [0] * (ma+1)
    result = []
    for i in arr:
        carr[i] += 1
    
    for i in range(len(carr)-1,0,-1):
        result += ([i] * carr[i])
    
    return result 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    p = arr[0]
    tail = arr[1:]

    right = [i for i in tail if i <= p]
    left = [i for i in tail if i > p]

    return quick_sort(left) + [p] + quick_sort(right)

#------------------------
# 3
# 15
# 27
# 12
#------
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

# insert_sort(arr)
# selection_sort(arr)
# arr = count_sort(arr)
# arr = quick_sort(arr)

arr.sort(reversed=True)

print(arr)
