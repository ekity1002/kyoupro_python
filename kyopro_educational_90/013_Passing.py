import heapq
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a,b,c = map(int, input().split())
    G[a-1].append((b-1,c))
    G[b-1].append((a-1,c))



def dk(k):
    """ダイクストラ法で検索"""
    INF = 10**9
    dist = [INF]*N # dist[i][j] 頂点iからj に向かうときの最短距離
    dist[k] = 0

    hq = []
    heapq.heapify(hq)
    for v in range(N):
        # 初期値を入れておく
        # tupleの最小値：要素の小さい方から比較する?
        heapq.heappush(hq, (dist[v], v))

    flags = [False]*N

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

    return dist

### おそい！！！
# for k in range(N):
#     if dist[0][k] != INF and dist[k][N-1] != INF:
#         print(dist[0][k] + dist[k][N-1])
#         continue
#     hq1 = make_hq(k)
#     hq2 = make_hq(0)
#     dk(hq1, 0)
#     dk(hq2, k)
#     print(dist[0][k] + dist[k][N-1])

dist_from_1 = dk(0)
dist_from_N = dk(N-1)
for k in range(N):
    print(dist_from_1[k] + dist_from_N[k])
