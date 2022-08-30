N,K = map(int, input().split())
L = list(map(int, input().split()))

# x本用意できるとする

def f(x):
    """1本の長さx 用意できる本数"""
    total = 0
    for l in L:
        total += l // x
    return total

left = 0
right = 100000 * 100000 + 1
eps = 10e-8
while abs(right-left) > eps:
    mid = (right + left) / 2 #長さ
    if f(mid) >= K:
        left = mid
    else:
        right = mid
    print(left, right)
print(left)