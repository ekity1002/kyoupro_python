N,M = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))

dp = [[-1] * (M+1) for _ in range(N+1)]

dp[0][0] = 0

for i in range(N):
    for j in range(0, M+1):   

        # i番目のボールを拾わない場合     
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])

        # 拾う場合
        if j+W[i] <= M:
            dp[i+1][j+W[i]] = max(dp[i][j+W[i]], dp[i][j]+V[i])

print(max(dp[-1]))