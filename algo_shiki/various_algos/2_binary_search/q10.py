N,X = map(int, input().split())

def f(x):
    """x以下の数値の数"""
    cnt = 0
    for i in range(N):
        cnt += min(N, int(x/(i+1)))
    return cnt


left = 0
right = N*N + 1
while abs(left-right) != 0:
    mid = (left+right)//2
    if f(mid) >= X:
        right = mid
    else:
        left = mid+1

print(left)

