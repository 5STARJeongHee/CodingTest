#그리드 문제

N = map(int, input())
travelers = list(map(int, input().split()))

travelers.sort()
print(travelers)

grp = 0
grp_list = []
for i in travelers:
    grp_list.append(i)
    if max(grp_list) <= len(grp_list):
        grp += 1
        grp_list = []

print(grp)
