from pdb import set_trace as st


#max = N*N

def f(mid, A, L,K):
    """
    最も短いものの長さ=mid のとき
    スコアを求める関数
    """
    ans = 0
    left=0
    for a in A:
        if (a - left) >= mid:
            ans += 1
            left = a
    if L - left >= mid:
        ans+=1
    return (ans >= K+1)

N,L = list(map(int, input().split()))
K = int(input())
A = list(map(int, input().split()))

left = 0
right = L+2
while right-left>1:
    mid = (right+left) // 2
#    st()
    flg = f(mid, A, L, K)
    if flg:
        left = mid
    else:
        right = mid
print(left)