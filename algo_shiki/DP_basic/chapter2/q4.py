N = int(input())
dp = [[1]*N for _ in range(N)]

for i in range(1,N):
    for j in range(N):
        if j==0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[-1][-1])
