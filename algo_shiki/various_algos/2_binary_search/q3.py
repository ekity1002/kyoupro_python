N,M = map(int ,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def f(x,k):
    if A[x] < B[k]:
        return False
    return True

for k in range(M):
    left = 0
    right = N
    while abs(right-left) != 0:
        mid = (left+right) // 2
        #print(mid)
        #print(k, left, right, mid, flush=True)
        if f(mid, k):
            right = mid
        else:
            left = mid+1
    print(left)