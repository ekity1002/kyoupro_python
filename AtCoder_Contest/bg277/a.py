N, X = map(int, input().split())
P = list(map(int, input().split()))

for k, p in enumerate(P):
    if p == X:
        print(k + 1)
        break
