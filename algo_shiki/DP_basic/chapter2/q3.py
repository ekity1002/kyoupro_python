N = int(input())
A = [[0]*3 for _ in range(N)]
for i in range(N):
    A[i] = list(map(int, input().split()))

dp = [[0]*3 for i in range(N)]
dp[0] = A[0]

for i in range(1, N):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + A[i][0]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + A[i][1]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + A[i][2]
print(max(dp[-1]))