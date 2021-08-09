# https://programmers.co.kr/learn/courses/30/lessons/83201
# 최대 100개의 데이터를 전부다 살펴 보면서 최소, 최대, 개수를 봐야하는데 이정도면 for문을 3번 써도 문제는 없을듯하다
# def solution(scores):
#     answer = ''
#     cnt_arr = [0] * len(scores)
#     total_arr = [0] * len(scores)

#     for i in range(len(scores)):
#         min_val = 10000
#         max_val = -1
#         cnt = len(scores)
#         for j in range(len(scores)):
#             total_arr[i] += scores[j][i]
#             if scores[i][i] == scores[j][i]:
#                 cnt_arr[i] += 1
#             if scores[j][i] < min_val:
#                 min_val = scores[j][i]
#             if scores[j][i] > max_val:
#                 max_val = scores[j][i] 
#         if min_val == scores[i][i] and cnt_arr[i] == 1:
#             total_arr[i] = (total_arr[i] - min_val) / (cnt - 1)
#         elif max_val == scores[i][i] and cnt_arr[i] == 1:
#             total_arr[i] = (total_arr[i] - max_val) / (cnt - 1)
#         else:
#             total_arr[i] = total_arr[i] / cnt
#     for i in total_arr:
#         if i >= 90:
#             answer+='A'
#         elif i >= 80:
#             answer += 'B'
#         elif i >= 70:
#             answer += 'C'
#         elif i >= 50:
#             answer += 'D'
#         else:
#             answer += 'F'    
#     return answer
## 다른사람 풀이
## zip 함수의 특징 - 같은 열의 데이터를 묶어주는 것을 이용하였음
from collections import Counter
def solution(scores):   
    answer = ''
    for idx, score in enumerate(list(map(list, zip(*scores)))):
        length = len(score)
        if Counter(score)[score[idx]] == 1 and (max(score) == score[idx] or min(score) == score[idx]):
            del score[idx]
            length -= 1

        grade = sum(score) / length

        if grade >= 90:
            answer += 'A'
        elif grade >= 80:
            answer += 'B'
        elif grade >= 70:
            answer += 'C'
        elif grade >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer



sc = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]

print(solution(sc))