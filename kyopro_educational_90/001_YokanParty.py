from pdb import set_trace as st

N,K = list(map(int, input().split()))

L = list(map(int, input().split()))


def f(x):
    ans = 0
    for l in L:
        ans += int(l/x)
    return ans
    
#print(A)
left = 0
right = 2e5
while right - left > 1e-8:
    mid = (left+right) / 2
    if f(mid) >= K:
        #st()
        left = mid
    else:
        #st()
        right = mid
print(left)