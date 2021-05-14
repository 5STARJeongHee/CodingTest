array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8] 

def quick_sort(array, start, end):
    if start >=end: # 원소가 1개인 경우 종료
        return
    
    pivot = start # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 큰 걸 찾으면 left에 저장된 index 값에 선택되어 있음

        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right: # 엇갈릴 경우 작은 데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않은 경우 작은 데이터와 큰 데이터 교체
            array[left],array[right] = array[right],array[left]
       
    quick_sort(array, start, right -1) 
    quick_sort(array, right+ 1, end)
    
def quick_sort_short(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    return quick_sort_short(left_side) + [pivot] + quick_sort_short(right_side)

# quick_sort(array, 0, len(array) -1)
array = quick_sort_short(array)
print(array)