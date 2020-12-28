from itertools import permutations
# permutations 함수를 사용하는 경우 
# - input: list, 조합수 
# - output: 조합수 만큼의 순열을 반환
a = []

items = [1,2,3,4]
for i in range(1, len(items) +1 ):
    for j in list(permutations(items,i)):
        a.append(j)

print(a)

#중복 순열(=product)
from itertools import product
print("case 1")
for i in product([1,2,3],'ab'):
    print(i, end=" ")

print("case 2")
for i in product(range(3), range(3), range(3)):
    print(i, end=" ")

print("case3")
for i in product([1,2,3], repeat=2):
    print(i, end=" ")

print("case4")
for i in product([1,2,3], repeat=3):
    print(i, end=" ")


# 구현 permutations
def perm(lst,n):
	ret = []
	if n > len(lst): return ret #수의 종류보다 조합수가 더 큼 -불가능

	if n==1: # 1개 일 때, 재귀 스택의 마지막 반환점
		for i in lst:
			ret.append([i])
	elif n>1:
        #permutation([1,2,3,4],2) = ([1] + permutation([2,3,4],1)) and
        #([2] + permutation([1,3,4],1)) and ([3] + permutation([1,2,4],1)) and
        #([4] + permutation([1,2,3],1))
        
		for i in range(len(lst)):
			temp = [i for i in lst]
			temp.remove(lst[i])
			for p in perm(temp,n-1):
				ret.append([lst[i]]+p)

	return ret

    #dfs 구현 방식
    def dfs_perm(lst,n):
	ret = []
	idx = [i for i in range(len(lst))]

	stack  = []
	for i in idx:
		stack.append([i])
	
	while len(stack)!=0:
		cur = stack.pop()

		for i in idx:
			if i not in cur:
				temp=cur+[i]
				if len(temp)==n: 
					element = []
					for i in temp:
						element.append(lst[i])
					ret.append(element)
				else:
					stack.append(temp)
	return ret
