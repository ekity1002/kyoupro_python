# マス目の経路最適化
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

dp = [[0] * N for _ in range(3)]
# dp[0][0] = 0
# dp[1][0] = 0
# dp[2][0] = 0

for i in range(N - 1):
    dp[0][i + 1] = min(
        dp[0][i] + (abs(A[i + 1] - A[i])),
        dp[1][i] + (abs(A[i + 1] - B[i])),
        dp[2][i] + (abs(A[i + 1] - C[i])),
    )
    dp[1][i + 1] = min(
        dp[0][i] + (abs(B[i + 1] - A[i])),
        dp[1][i] + (abs(B[i + 1] - B[i])),
        dp[2][i] + (abs(B[i + 1] - C[i])),
    )
    dp[2][i + 1] = min(
        dp[0][i] + (abs(C[i + 1] - A[i])),
        dp[1][i] + (abs(C[i + 1] - B[i])),
        dp[2][i] + (abs(C[i + 1] - C[i])),
    )

# from pprint import pprint
# pprint(dp)
print(min(dp[0][N - 1], dp[1][N - 1], dp[2][N - 1]))
