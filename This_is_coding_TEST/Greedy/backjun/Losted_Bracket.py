#연산자 +연산을 먼저 수행
import re

text = input()
n = list(map(int,re.split('[-+]',text)))
exp = list(map(str, re.split('\d{1,5}',text)))
exp.remove('')
exp.remove('')


i=0
while exp.count("+") != 0:
    e = exp.pop(i)
    temp = 0
    if e == '+':
        temp += n.pop(i) + n.pop(i)
        n.insert(i,temp)
        
    if e == '-':
        exp.insert(i,'-')
        i += 1
ret = n[0]
for i in range(1,len(n)):
    ret -= n[i]

print(ret)
    
    

