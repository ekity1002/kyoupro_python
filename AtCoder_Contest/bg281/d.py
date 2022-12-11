#
N, K, D = map(int, input().split())
A = list(map(int, input().split()))

dp = [[[[-1] * D] * (K + 1)] * (N + 1)]
print(dp)
# a1...ai から j こえらんだとき、Dでわったあまりがk であるときの最大値
dp[0][0][0] = 0

for i in range(N):
    for j in range(K):
        for k in range(D):
            if dp[i][j][k] == -1:
                continue

            # a_iをえらばない場合
            dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])

            # a_i を選ぶ
            if j != k:
                dp[i + 1][j + 1][(k + A[i]) % D] = max(
                    dp[i + 1][j + 1][(k + A[i]) % D], dp[i][j][k] + A[i]
                )
