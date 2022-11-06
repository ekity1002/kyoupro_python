# 連続ボーナスのある買い物(1)
N, A = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

INF = 10**9
dp = [[INF] * 3 for i in range(N)]
dp[0][0] = P[0]
dp[0][1] = Q[0]  # (金額、連続数)
dp[0][2] = R[0]  # (金額、連続数)
S = []
S.append(P)
S.append(Q)
S.append(R)

from pdb import set_trace as st

# st()
for i in range(1, N):
    for j in range(3):
        # 手前のステップで最も安い店
        cost = INF
        for k in range(3):
            p = dp[i - 1][k]
            if k == j:
                cost = min(cost, p + S[j][i] - A)
            else:
                cost = min(cost, p + S[j][i])

        dp[i][j] = cost
# print(dp)
print(min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))
10011