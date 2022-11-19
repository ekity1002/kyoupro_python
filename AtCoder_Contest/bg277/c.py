import sys
from collections import defaultdict, deque

N = int(input())
G = defaultdict(list)
for i in range(N):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

S = {1}
que = deque([1])
while que:
    v = que.popleft()
    for nv in G[v]:
        if not nv in S:
            S.add(nv)
            que.append(nv)
print(max(S))
