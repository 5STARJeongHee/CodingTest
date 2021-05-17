N = int(input())
d = list(map(int, input().split()))[:N]

def quick_sort(array, start, end):
    if start < end: # 원소가 1개인 경우 종료
        i = start - 1 # 벽 하나, 벽 왼쪽은 모두 피벗보다 작음
        p = array[end]
        
        for j in range(start,end):
            if array[j] < p:
                i += 1
                array[i], array[j] = array[j], array[i] # 피벗 보다 작은 것들을 벽 왼쪽에 쌓아가면 자연스레 벽 오른쪽은 피벗보다 큰 값이 모임
        i += 1 # 현제 벽을 포함 왼쪽은 작은 곳이고 오른쪽은 큰쪽이니, 바로 오른 쪽에 있는 것과 피벗과 교환하면 완성
        array[i], array[end] = array[end], array[i] # 

        for j in d:
            print(j,end=' ')
        print()   

        quick_sort(array, start, i-1) 
        quick_sort(array, i+1, end)

quick_sort(d, 0, len(d)-1)
