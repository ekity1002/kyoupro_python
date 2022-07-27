N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

def f(x,k):
    return A[x] <= B[k]

for k in range(M):
    left = 0
    right = N
    while abs(right-left) >= 1:
        mid = (left+right)//2
        if f(mid, k):
            left = mid+1
        else:
            right = mid
    print(left)
