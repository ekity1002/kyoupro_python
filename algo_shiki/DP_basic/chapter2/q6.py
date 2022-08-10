N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

def check(dp, i,j):
    if not (0 <= i <= N and 0 <= j <= N):
        return 0
    return dp[i][j]

for i in range(N):
    for j in range(N):
        dp[i][j] = A[i][j] + max(check(dp, i-1, j), check(dp, i, j-1))

# from pprint import pprint
# pprint(A)
# pprint(dp)
print(dp[-1][-1])