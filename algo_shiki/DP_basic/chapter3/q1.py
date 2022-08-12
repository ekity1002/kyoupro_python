N,M = map(int, input().split())
A = list(map(int, input().split()))
dp = [[False]*M for _ in range(N)]
dp[0][0] = True

def check(i, j):
    return (0 <= i < N and 0 <= j < M)

from pdb import set_trace as st
for i in range(N):
    for j in range(M):
        #st()
        if dp[i][j]:
            if check(i+1, j): dp[i+1][j] = True
            if check(i+1, j+A[i]): dp[i+1][j+A[i]] = True

ans = 0
for i in range(M):
    if dp[-1][i]: ans+=1
print(ans)
