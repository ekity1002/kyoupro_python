N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[-1]* (M+1) for _ in range(N+1)]
dp[0][0] = 0 

for i in range(N):
    for j in range(M+1):
        if dp[i][j] < 0: continue

        # A[i] 選ばない場合
        if dp[i+1][j] >= 0:
            dp[i+1][j] = min(dp[i][j], dp[i+1][j])
        else:
            dp[i+1][j] = dp[i][j]

        # 選ぶ場合
        if j + A[i] <= M:
            dp[i+1][j+A[i]] = dp[i][j] + 1
# from pprint import pprint
# pprint(dp)
# ans = 0
# for i in range(N+1):
#     if dp[i][-1] >= 0:
#         ans += dp[i][-1]
# print(ans)
print(dp[-1][-1])