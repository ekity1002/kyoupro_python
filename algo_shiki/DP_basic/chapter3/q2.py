N,M = map(int, input().split())
W = list(map(int, input().split()))
dp = [[False]*(M+1) for _ in range(N+1)]
dp[0][0]=True

def check(i,j):
    return (0<=i< N+1 and 0<=j<M+1)

from pdb import set_trace as st
for i in range(N):
    for j in range(M+1):
        # if i==N:
        #     st()
        if dp[i][j]:
            if check(i+1, j): dp[i+1][j] = True
            if check(i+1, j+W[i]): dp[i+1][j+W[i]] = True

#from pprint import pprint
#pprint(A)
#pprint(dp)

print('Yes' if dp[-1][M] else 'No')

