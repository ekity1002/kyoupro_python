# DPの問題
N = int(input())
S = input()
A = 'atcoder'
MOD=10**9 + 7

# dp[i][j] S[i] までに atcoder の j文字目までが完成している選び方の数
dp = [[0]*(len(A)+1) for i in range(N+1)]
dp[0][0] = 1

def mod(a,b):
    ret = a + b
    if ret >= MOD:
        ret = ret - MOD
    return ret

for i in range(N):
    for j in range(len(A)+1):

        # S[i] を選ばない場合
        dp[i+1][j]  = mod(dp[i][j], dp[i+1][j])

        # S[i] を選ぶ場合
        if j < len(A) and S[i] == A[j]:
            dp[i+1][j+1] = mod(dp[i][j], dp[i+1][j+1])

#from pprint import pprint
#pprint(dp)

print(dp[N][-1])