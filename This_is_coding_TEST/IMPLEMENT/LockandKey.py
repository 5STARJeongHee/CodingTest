# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
# key_l = len(key)
# ones = [[1] * key_l for _ in range(key_l)]

# def rotation(k):
#     N = len(k)
#     ret = [[0] * N for _ in range(N)]

#     for r in range(N):
#         for c in range(N):
#             ret[c][N-1-r] = k[r][c]

#     return ret


# def move(k, dir=[1, 0]):
#     N = len(k)
#     ret = [[0] * N for _ in range(N)]
#     for f in range(N):
#         for s in range(N):
#             if f + dir[0] < 0 or f + dir[0] >= N or s + dir[1] < 0 or s + dir[1] >= N:
#                 continue
#             else:
#                 ret[f + dir[0]][s + dir[1]] = k[f][s]
#     return ret


# def match(k, l):
#     N = len(k)
#     b = True
#     for f in range(N):
#         for s in range(N):
#             if k[f][s] == l[f][s]:

#                 b = b and False
#             else:
#                 b = b and True
#     return b


# def print_key(k):
#     for i in k:
#         print(i)


# def find(key, lock):
#     t = False
    
#     for i in range(4):
#         key = rotation(key)
#         for d in dir:
#             m_key = move(key,d)
#             print_key(m_key)
#             print()

#             t = match(m_key,lock)
#             if match(m_key, ones) == True:
#                 break
#             if t == False:
#                 t = find(m_key,lock)
#             elif t == True:
#                 return t
            
#     return t 

# print(find(key,lock))

# 동빈좌 답안
# 2차원 리스트 90도 회전하기
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어 맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False
