# 다른 사람 코드 사용
# def solution(rows, columns, queries):
#     answer = []
#     org = [[rows*i + j for j in range(1,rows+1)] for i in range(rows)]
#     for i in queries:
#         answer.append(rotate(org,i))
#     return answer

# def rotate(arr,points):
#     temp = arr.copy()
#     a,b,c,d = points
#     top = a-1
#     left = b-1
#     bottom = c-1
#     right = d-1
#     m = 10000
#     for i in range(left,right):
#         arr[top][i+1] = arr[top][i]
#         m = min(m,arr[top][i+1])
#     for i in range(top,bottom):
#         arr[i+1][right] = arr[i][right]
#         m = min(m,arr[i+1][right])
#     for i in range(right,left,-1):
#         arr[bottom][i-1] = arr[bottom][i]
#         m = min(m,arr[bottom][i-1])
#     for i in range(bottom,top,-1):
#         arr[i-1][left] = arr[i][left]
#         m = min(m,arr[i-1][left])
#         print(arr)
#     return m
def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for col in range(columns)] for row in range(rows)]

    val = 1
    for i in range(0, rows):
        for j in range(0, columns):
            matrix[i][j] = val
            val+=1

    for a,b,c,d in queries:
        top = a-1
        left = b-1
        bottom = c-1
        right = d-1
        first = matrix[top][left]
        m = first
        for i in range(top,bottom):
            matrix[i][left] = matrix[i+1][left]
            m = min(m,matrix[i][left])
        for i in range(left,right):
            matrix[bottom][i] = matrix[bottom][i+1]
            m = min(m,matrix[bottom][i])
        for i in range(bottom,top,-1):
            matrix[i][right] = matrix[i-1][right]
            m = min(m,matrix[i][right])
        for i in range(right,left,-1):
            matrix[top][i] = matrix[top][i-1]
            m = min(m,matrix[top][i])
        matrix[top][left+1] = first 
    
        answer.append(m)

    return answer
print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))