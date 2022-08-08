# 木の高さの最小値
N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

seen = [0]*N
from queue import Queue
def bfs(s):
    dist = [-1]*N
    dist[s] = 0

    que = Queue()
    que.put(s)
    while not que.empty():
        v = que.get()
        seen[v] = 1
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v]+1
                que.put(nv)
        
    return dist

#max_info = [-1,-1]
dist = bfs(0)
e1 = dist.index(max(dist))
dist2 = bfs(e1)

import math
d = math.ceil(max(dist2) / 2)
print(d)