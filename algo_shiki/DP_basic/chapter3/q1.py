N, M = map(int, input().split())
A = list(map(int, input().split()))
dp = [[0] * M for _ in range(N)]
dp[0][0] = 1
# from pdb import set_trace as st

for i in range(N - 1):
    for j in range(M):
        # st()
        dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])
        if j + A[i] < M:
            dp[i + 1][j + A[i]] = max(dp[i][j], dp[i][j + A[i]])
# print(dp)
print(sum(dp[-1]))
