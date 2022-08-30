N = int(input())
X = list(map(int, input().split()))
#print(X)
MAX = 10**18+1

def f(x):
    """x日目の貯金額"""

    return x*(x+1)/2


for k in range(N):
    left = 1
    right = MAX
    if X[k] == 1:
        print(1)
        continue
    while abs(left - right) != 0:
        mid = (right+left) // 2
        if f(mid) >= X[k]:
            right = mid
        else:
            left = mid + 1
        # print(left, right)
    print(left)
