array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1,len(array)): # 앞에는 정렬되어 있으며 첫카드가 정렬되었다는 가정으로 시작
    for j in range(i,0,-1): # 삽입할 카드로 왼편의 정렬된 카드들과 비교 시작
        if array[j] < array[j-1]:
            array[j],array[j-1] = array[j-1], array[j] # 삽입할 카드가 왼편에 비교 한 카드보다 작으면 앞에 삽입
        else: # 자기보다 작은 카드 없음 종료
            break 
print(array)