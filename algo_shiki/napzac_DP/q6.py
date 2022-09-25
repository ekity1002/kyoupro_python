# 6：K 個以内部分和問題
N,M,K = map(int, input().split())
A = list(map(int, input().split()))
INF=10**9
dp = [[INF]*(M+1) for _ in range(N+1)]
dp[0][0] = 0 #dp[i][j] 数字Ai, 

for i in range(N):
    for j in range(M):

        # 選ばない場合
        dp[i+1][j] = min(dp[i][j], dp[i+1][j])

        # 選ぶ場合
        if j + A[i] <= M:
            dp[i+1][j+A[i]] = min(dp[i][j+A[i]], dp[i][j]+1)

#print(dp)
# from pdb import set_trace as st
# st()
for i in range(N+1):
    if dp[i][-1] <= K:
        print('Yes')
        break
else:
    print('No')