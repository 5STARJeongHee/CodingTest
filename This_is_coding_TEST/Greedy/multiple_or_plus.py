#그리드 문제 18분

S = input()
Num = []

for i in S:
    Num.append(int(i))

op_len = len(Num) -1
op = []
for i in range(op_len):
    if Num[i] == 0:
        op.append('+')
    else:
        op.append('x')

for i in range(len(op)):
    if op[i] == '+':
        Num[i+1] = Num[i] + Num[i+1]
    else:
        Num[i+1] = Num[i] * Num[i+1]

print(Num[len(Num)-1])
