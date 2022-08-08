N = int(input())
W = list(map(int, input().split()))
W2 = sorted(W)

from bisect import bisect_left
for k in range(N):
    print(bisect_left(W2, W[k]))

