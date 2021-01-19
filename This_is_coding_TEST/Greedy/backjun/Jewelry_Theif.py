import sys, os
from queue import PriorityQueue
# python 입력 속도 비교 
# https://www.acmicpc.net/blog/view/56

N,K = map(int,sys.stdin.readline().split())
jewelry = []

for i in range(N): # 보석 무게 - 값
    temp = list(map(int,sys.stdin.readline().split()))
    jewelry.append(temp)

for i in range(K): # 주머니 무게 - 값 무한
    jewelry.append([int(sys.stdin.readline()),20000000])

pocket = PriorityQueue()
jewelry.sort() # 무게가 가벼운 순부터
ret = 0
for a in jewelry:
    if a[1] != 20000000: # 주머니를 열지 않았을 때, 임시 주머니에서 가격을 재봄
        pocket.put(-a[1])
    else: # 주머니를 열었을 때 임시 주머니에서 가장 비싼 보석을 꺼냄냄
        if not pocket.empty(): #무게가 가벼운 주머니를 열 때 임시 주머니에 있는 보석들은 가벼운 주머니보다 작다
            ret += -pocket.get()

print(ret)

    