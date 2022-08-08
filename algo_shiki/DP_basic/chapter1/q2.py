N = int(input())
A = list(map(int , input().split()))
T = [-1] * N

for i in range(N):
    if i == 0:
        T[i] = 0
    elif i==1:
        T[i] = A[i]
    else:
        T[i] = min(T[i-2] + 2*A[i], T[i-1] + A[i])
print(T[N-1])