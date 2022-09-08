N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[-1] * (M+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(M+1):
        if dp[i][j] < 0:
            continue

        # A[i] を選ばない
        dp[i+1][j] = dp[i][j]

        # A[i] を選べる場合
        if j + A[i] <= M:
            dp[i+1][j+A[i]] = dp[i][j] + A[i]
        
# from pprint import pprint
# pprint(dp)
print('Yes' if dp[-1][-1] >= 0 else 'No')