# 점화식 a_i = max(a_(i-1), a_(i-2) + k_i)
# 현제 i번째 창고를 털건데 바로 이전 항의 참고하면 현제 항은 못 털고, 2칸 뒤의 것을 고르면 현제의 것과 그 이전의 것을 참고해서 
# 털 수 있다.
N = int(input())
k_lst = list(map(int, input().split()))
d_arr = [0] * 100
d_arr[0] = k_lst[0]
d_arr[1] = max(k_lst[0],k_lst[1])
for i in range(3,N):
    d_arr[i] = max(k_lst[i-1],k_lst[i-2] + k_lst[i])

print(d_arr[N-1])

