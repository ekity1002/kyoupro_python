# ダイクストラ法高速化
# 最小値を持つ頂点をヒープを使って検索する
# ヒープ：最小（最大値）を高速に検索(logN), 要素の挿入が(logN)で可能
# O((N+M)log(N+M))

import heapq
N,M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    u,v,w = map(int, input().split())
    G[u].append((v,w))

INF=10**9
dist = [INF]*N
dist[0] = 0
flags = [False]*N

# ヒープ
hq = [] #(仮の最短距離、頂点番号) を管理するヒープ
heapq.heapify(hq)
for v in range(N):
    # 初期値を入れておく
    heapq.heappush(hq, (dist[v], v))


while len(hq) > 0:
    # ヒープの最小値を取り出す
    [d,v] = heapq.heappop(hq)
    # vの最短距離が確定してるなら何もしない
    if flags[v] : continue

    for nv, w in G[v]:
        # 距離の更新がある場合には、ヒープに更新後の情報を入れる        
        dist[nv] = min(dist[nv], dist[v]+w)
        heapq.heappush(hq, (dist[nv], nv))
        
    flags[v] = True

for i in range(N):
    print(dist[i])