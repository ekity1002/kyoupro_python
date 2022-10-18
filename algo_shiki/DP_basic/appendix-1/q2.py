# 入力を受け取る
N, A, B = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

S = [P, Q, R]

# DP テーブルと初期化に使う大きな数
INF = 1 << 30
dp = [[[INF for _ in range(4)] for _ in range(3)] for _ in range(N)]

# DP 初期条件
for s in range(3):
    dp[0][s][1] = S[s][0]

# DP テーブルの更新
for i in range(1, N):
    for s in range(3):
        # dp[i][s][1] を求める
        cost = INF
        for ps in range(3):
            # d = 1 のため、前日に訪れた店 ps は 今日訪れた店 s と異なる
            if ps == s:
                continue
            for pd in range(1, 4):
                cost = min(cost, dp[i - 1][ps][pd])
        dp[i][s][1] = cost + S[s][i]
        # dp[i][s][2] を求める
        dp[i][s][2] = dp[i - 1][s][1] + (S[s][i] - A)
        # dp[i][s][3] を求める
        dp[i][s][3] = min(dp[i - 1][s][2], dp[i - 1][s][3]) + (S[s][i] - B)

# 答えを出力する
ans = INF
for s in range(3):
    for d in range(1, 4):
        ans = min(ans, dp[N - 1][s][d])
print(ans)
