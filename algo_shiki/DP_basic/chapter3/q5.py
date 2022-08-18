from pprint import pprint
#pprint(dp)
from pdb import set_trace as st

N, M = map(int, input().split())
W = list(map(int, input().split()))

INF=100_000_000_0
dp = [[INF]*(M+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(M+1):
        if dp[i][j]==INF:
            continue

        # ボールiを拾わない場合
        dp[i+1][j] = min(dp[i][j], dp[i+1][j])

        # ボールiを拾う場合
        if j + W[i] <= M:
            dp[i+1][j+W[i]] = min(dp[i][j+W[i]], dp[i][j]+ 1)

#pprint(dp)

print(dp[N][M] if dp[N][M] != INF else -1)