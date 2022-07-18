from queue import Queue
N, M = map(int, input().split())
G = [[] for _ in range(N)]
seen = [False for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)



dist = [-1] * N # 各頂点がなんて目に検索されたか
nodes = [[] for i in range(N)] #k手目に探索された頂点集合を格納
dist[0] = 0 #初期化
nodes[0] = [0]

for k in range(1, N): # k回目の探索
    for v in nodes[k-1]: #しらべる頂点
        for next_v in G[v]:#調べる頂点と隣り合っている超ｔん
            if dist[next_v] != -1:
                # 探索済みなら何もしない
                continue
            dist[next_v] = dist[v] + 1
            nodes[k].append(next_v)

for k in range(N):
    nodes[k].sort()
    print(*nodes[k])

