N = int(input())
A = [[0]*N for _ in range(N)]
A[0] = list(map(int, input().split()))
#print(A)

for i in range(1, N):
    for j in range(N):
        if j==0:
            A[i][j] = (A[i-1][j] + A[i-1][j+1]) % 100
        elif j==N-1:
            A[i][j] = (A[i-1][j] + A[i-1][j-1]) % 100
        else:
            A[i][j] = (A[i-1][j+1] + A[i-1][j] + A[i-1][j-1]) % 100
        
print(A[-1][-1])