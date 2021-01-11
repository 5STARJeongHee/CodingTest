N = int(input())

temp = list()

while N != 0 :
    t = int(N%10)
    N = int(N/10)
    temp.append(t)

left = 0
right = 0
half = int(len(temp)/2)

for i in range(half):
    left += temp[i]
    right += temp[i+half]

if left == right:
    print("LUCKY")
else:
    print("READY")