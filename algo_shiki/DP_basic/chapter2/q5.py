N = int(input())
S = []
for _ in range(N):
    S.append(input())

#print(S)
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

def check(dp, i,j):
    if not (0 <= i <= N and 0 <= j <= N):
        return 0
    if S[i][j] == "#":
        return 0
    return dp[i][j]

for i in range(N):
    for j in range(N):
        up = check(dp, i-1, j)
        left = check(dp, i, j-1)
        #print(i,j, up, left)
        dp[i][j] = dp[i][j] + up + left

print(dp[-1][-1])