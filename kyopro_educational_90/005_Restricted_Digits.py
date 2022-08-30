# ダブリング, DP
# N桁、Bの倍数, Kこの整数
N,B,K = map(int, input().split())
C = list(map(int, input().split()))

MOD = 1000000000 + 7

dp = [[0] * 10 for _ in range(N+1)]
#dp[0][0] = 0
for i in range(N):
    for c in C:
        r = (10**i + c) % B
        dp[i+1][c] = (dp[i][c] + r) % MOD