N,M = map(int, input().split())

def f(x):
    yokin = N
    for _ in range(5):
        yokin +=1
        yokin = yokin*x
    yokin+=1
    return yokin < M

left = 0
right = 1e6
eps=1e-5
while abs(right-left) > eps:
    mid = (left+right)/2
    if f(mid):
        left = mid
    else:
        right = mid

print(left)
