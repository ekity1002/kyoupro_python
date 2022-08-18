N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[-1]*M for _ in range(N)]
# print(dp)
dp[0][0] = 0
# from pdb import set_trace as st
# st()
from pprint import pprint
for i in range(N-1):
    for j in range(M):
        if dp[i][j] < 0:
            continue

        dp[i+1][j] = max(dp[i][j], dp[i+1][j])

        if j+A[i] < M:
            dp[i+1][j+A[i]] = max(dp[i][j]+B[i], dp[i+1][j+A[i]])

print(dp[N-1][M-1])