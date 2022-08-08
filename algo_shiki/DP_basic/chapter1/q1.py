N,X,Y = map(int, input().split())
A = [-1] * N
for i in range(N):
    if i==0:
        A[i]=X
    elif i==1:
        A[i]=Y
    else:
        A[i] = (A[i-1] + A[i-2]) % 100
print(A[N-1])
