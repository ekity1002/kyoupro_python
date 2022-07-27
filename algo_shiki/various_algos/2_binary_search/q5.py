N,K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# print('='*40)
# print(A)
def f(i,j):
    return A[i] + A[j] >= K

ans = 0
for i in range(N):
    left = i
    right = N
    while abs(right-left) >= 1:
        mid = (left+right) // 2
        if f(i, mid):
            right = mid
        else:
            left = mid + 1
    #print(left)

    ans += (N-left)*2
    if left==i:
        ans -=1

#print('='*40)

print(ans)    

