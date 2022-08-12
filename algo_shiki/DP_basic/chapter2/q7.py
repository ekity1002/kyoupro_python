N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dp = [[100_000_000]*N for _ in range(N)]

def check(dp, i,j):
    if not (0 <= i < N and 0 <= j < N):
        return 1e10
    return dp[i][j]

from pdb import set_trace as st
for i in range(N):
    for j in range(N-1, -1, -1):
        #st()
        if i==0 and j==N-1:
            dp[i][j] = A[i][j]
        else:
            dp[i][j] = A[i][j] + min(check(dp, i-1, j), check(dp, i, j+1))

# from pprint import pprint
# pprint(A)
# pprint(dp)
print(dp[-1][0])