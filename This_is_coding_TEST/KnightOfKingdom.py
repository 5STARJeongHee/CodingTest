#왼쪽 위아래, 오른쪽 위아래, 위쪽 좌우, 아래쪽 좌우
h = [-2, -2, 2, 2, -1, 1,-1, 1]
v = [-1 , 1, -1, 1,-2,-2, 2, 2]

limit = 8
#x 좌표 매핑용
h_map = ['a','b','c','d','e','f','g','h']

data = input()
x=0
y=int(data[1])

answer = 8
# x좌표 매핑
for i in h_map:
    if data[0] == i:
        x = h_map.index(i)+1

for k in range(8):
    #매번 좌표 초기화
    tx = x
    ty = y
    #말을 움직이고 나서의 좌표
    tx += h[k]
    ty += v[k]
    
    if tx <1 or tx>8 or ty <1 or ty>8:
        answer -=1
    
print(answer)