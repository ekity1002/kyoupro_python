# ダイクストラ法
# グラフの辺の重みがすべて非負であることが保証されている場合には、 より高速な最短経路アルゴリズム 
N,M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    u,v,w = map(int, input().split())
    G[u].append((v,w))

INF=10**9
dist = [INF]*N
dist[0] = 0
flags = [False]*N

def get_min_idx(dist, flags):
    val = INF
    min_idx = -1
    for i in range(N):
        if not flags[i] and val > dist[i]:
            val = dist[i]
            min_idx = i
    return min_idx

while 1:
    v = get_min_idx(dist, flags)
    if v == -1:
        break

    for nv, w in G[v]:
        dist[nv] = min(dist[nv], dist[v]+w)
        
    flags[v] = True

for i in range(N):
    print(dist[i])