from collections import Counter

H, W = map(int, input().split())
# ls1 = [[] for _ in range(W)]
# ls2 = [[] for _ in range(W)]
# d1 = dict()
# d2 = dict()
counts = []
for _ in range(H):
    counts.append(Counter(input()))

ans = "Yes"
for c in counts:
    if c != Counter(input()):
        ans = "No"
        break

print(ans)
