import re
s = input()

arr = list()
a = '[0-9]'
for i in s:
    arr.append(i)

arr.sort()
num = 0
S = ''
for i in arr:
    if re.match(a,i):
        num += int(i)
    else:
        S+=i

ret = S+str(num)
print(ret)