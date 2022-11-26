N, M = map(int, input().split())
W = list(map(int, input().split()))
dp = [[0] * (M + 1) for i in range(N + 1)]
dp[0][0] = 1

from pdb import set_trace as st

for i in range(N):
    for j in range(M):
        # ボールiを拾わない場合
        dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])

        # 拾う場合
        if j + W[i] < M + 1:
            dp[i + 1][j + W[i]] = max(dp[i][j], dp[i][j + W[i]])

print("Yes" if dp[-1][M] else "No")
