# 이진 탐색 코드 (재귀)
# 탐색하려는 곳이 이미 정렬이 되어 있다는 가정하에 진행
def binary_search_self(array, target, start, end):
    if start > end: # 매번 start end가 넘어올때 end는 중간 인덱스보다 1적은데
        return None # 마지막 하나까지도 타겟이 없다면 start보다 end가 1 적어진다.
    mid = (start + end) //2 # 중간 인덱스
    if array[mid] == target:
        return mid # 타겟 인덱스 찾음
    elif array[mid] > target: # 중앙 인덱스 값이 target 보다 큼- 적은쪽으로
        return binary_search_self(array, target, start, mid -1)
    else:
        return binary_search_self(array, target, mid + 1, end)

def binary_search(array,target,start,end):
    while start <=end:
        mid = (start + end) //2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print('찾고자 하는 원소가 없음')
else:
    print(result+1,'이 찾고자 하는 인덱스입니다.')

    """
    10 7
    1 3 5 7 9 11 13 15 17 19
    """
"""
bisect_left(a,x)
bisect_right(a,x) - a 란 배열의 정렬된 순서를 유지하면서 x를 삽입할 제일 오른쪽 인덱스 반환
a = [1,2,4,4,8]
x = 4
bisect_left(a,x) - 2
bisect_right(a,x) - 4
"""