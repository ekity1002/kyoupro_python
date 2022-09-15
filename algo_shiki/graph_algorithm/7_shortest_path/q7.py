# Q7. ベルマン・フォード法総合
# N 回のステップが終了した時点における頂点 N−1 までの距離 dist_step[N][N-1] が初期値 INF のままであれば、 頂点 0 から頂点 N−1 への経路は存在しません。この場合は impossible を出力すればよいです。

# では負閉路が存在すれば必ず -inf であるかと言えば、そうではありません。 入出力例 4 のように、負閉路を経由して頂点 N−1 に到達できない可能性もあるからです。
# つまり -inf であるかを判定するためには、 負閉路に含まれる頂点から頂点 N−1 にたどり着くことができるかを確認する必要があります。

N,M = map(int, input().split())
E = []
G = [[] for i in range(N)]

for i in range(M):
    u,v,w = map(int, input().split())
    E.append([u,v,w])
    G[u].append((v,w))


def dfs(s):
    checked = [False] * N
    
    st = [s]
    while st:
        v = st.pop()
        checked[v] = True
        for nv, w in G[v]:
            if checked[nv]:
                continue
            st.append(nv)
    return checked


INF = 10**9
dist = [INF] * N
dist2 = [INF] * N
dist[0] = 0
dist2[0] = 0

for _ in range(N):
    before = dist.copy()
    for i in range(M):
        u,v,w = E[i]
        dist[v] = min(dist[v], dist[u] + w)
        dist2[v] = min(dist2[v], dist2[u] + abs(w))
# print(dist)
# print(dist2)
if dist2[N-1] == INF:
    print('impossible')
elif before != dist:
    # 負の頂点から, N-1にたどりつければ -inf
    for i in range(N):
        if dist[i] < 0:
            checked = dfs(i)
            if checked[-1]:
                print('-inf')
                exit()
    print(dist[N-1])
else:
    print(dist[N-1])
