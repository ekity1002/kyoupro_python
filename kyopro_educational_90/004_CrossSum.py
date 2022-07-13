
import sys
input = sys.stdin.readline
H, W = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]

w_sum = [sum(A[i]) for i in range(H)] #よこ
h_sum = [ sum([A[h][w] for h in range(H)])  for w in range(W)]
for h in range(H):
    for w in range(W):
        print(f'{h_sum[w] + w_sum[h] - A[h][w]} ', end='')
    print('')
