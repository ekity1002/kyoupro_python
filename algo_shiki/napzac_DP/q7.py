N,M = map(int, input().split())
A = []
B = []
for _ in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

# dp[i][j]: i番目までの整数の中から選んで総和をj とするときの A[i]の個数の最小値
INF = 10**10
dp = [[INF]*(M+2) for _ in range(N)]
dp[0][0] = 0
from pdb import set_trace as st
st()
for i in range(N):
    for j in range(M+1):
        # 選ばない場合:
        if dp[i][j] < INF: dp[i+1][j] = 0

        if j>=A[i]:
            if dp[i][j-A[i]] < INF:
                dp[i+1][j] = min(dp[i+1][j], 1)
            if dp[i+1][j-A[i]] < B[i]:
                dp[i+1][j] = min(dp[i+1][j], dp[i+1][j-A[i]] + 1)

if dp[N][M] < INF:
    print('Yes')
else:
    print("No")