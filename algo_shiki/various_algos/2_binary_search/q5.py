N,K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

def f(i,j):
    return A[i]+A[j] >= K

ans = 0
for i in range(N):
    left = 0
    right = N
    while abs(left-right) != 0:
        mid = (left+right)//2
        if f(i, mid):
            right = mid
        else:
            left = mid+1

    ans += (N-left)
print(ans)