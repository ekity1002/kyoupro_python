N = float(input())
eps=1e-5
def f(x):
    return x*(x*(x+1)+2) + 3 < N

left=0
right = 101
while abs(right-left) > eps:
    mid = (left+right) / 2
    #print(mid)
    if f(mid):
        left=mid
    else:
        right=mid

print(left)