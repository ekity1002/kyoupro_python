N, W_MAX = map(int, input().split())
W = []
V = []

for i in range(N):
    w,v = map(int, input().split())
    W.append(w)
    V.append(v)

from pdb import set_trace as st
dp = [[-1] * (W_MAX+1) for i in range(N+1)]
dp[0][0] = 0 #dp[i][j] i込めまでに選んだ品物の　重さが j であるときの価値の最大値

#st()
for i in range(N):
    for j in range(W_MAX):
        if dp[i][j] < 0:
            continue

        # 選ばない場合
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])

        if j+W[i] > W_MAX:
            continue
        
        # 選ぶ場合
        dp[i+1][j+W[i]] = max(dp[i][j+W[i]], dp[i][j] + V[i], dp[i][j])

# from pprint import pprint
# pprint(dp)
print(max(dp[-1]))