N,A,B = map(int, input().split())
X = list(map(int, input().split()))

M = list(map(lambda x: x%A, X))
#print(M)

dp = [[False]*(A) for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(A):
        if dp[i][j]:
            # Xiを選ぶ
            dp[i+1][j] = dp[i][j]
              
            # Xi を選ばない 
            # from pdb import set_trace as st
            # st()
            nj = (j + M[i]) % A
            # print(nj)
            dp[i+1][nj] = True

ans = 'No'
for i in range(N+1):
    if dp[i][B]:
        ans = 'Yes'

# from pprint import pprint
# pprint(dp)
print(ans)
