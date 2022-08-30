N = int(input())
W = list(map(int, input().split()))

MAX = 1000*50 + 1
dp = [[-1]*MAX for _ in range(N+1)]

# dp[i][j] = 総和の差分

dp[0][0] = sum(W) #一つも選んでいない状態の差分

from pdb import set_trace as st
for i in range(N):
    for j in range(MAX):
        if dp[i][j] < 0:
            continue

        #st()
        # W[i]を選ばない場合
        dp[i+1][j] = dp[i][j]

        # W[i] を選ぶ場合
        nj = j + W[i]
        dp[i+1][nj] = dp[i][j] - W[i]

from pprint import pprint
#pprint(dp)
#st()

ans = dp[0][0]
for i in range(MAX):
    one =  dp[-1][i]
    two = dp[0][0] - one
    diff = abs(one-two)
    if diff < ans: ans = diff
print(ans)

