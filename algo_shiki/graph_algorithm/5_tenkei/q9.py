
#サイクル検出: BFS
import sys
sys.setrecursionlimit(10**6)
from queue import Queue

N,M = map(int, input().split())
G = [[] for _ in range(N)]
deg = [0] * N #出自数格納配列

for _ in range(M):
    a, b = map(int, input().split())
    G[b].append(a) #終点とする辺のみを格納
    deg[a] += 1

for i in range(N):
    G[i].sort()

order = []
que = Queue()

for v in range(N):
    if deg[v] == 0:
        que.put(v)

while not que.empty():
    v = que.get()
    order.append(v)

    for nv in G[v]:
        deg[nv] -= 1
        if deg[nv] == 0:
            que.put(nv)

#print(order)
# 有向グラフを持つなら、同じ頂点が複数回参照されたり、含まれなかったりするはず
if len(order) != N:
    print('Yes')
else:
    print('No')

