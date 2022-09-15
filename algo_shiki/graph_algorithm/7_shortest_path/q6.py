# Q6. 負閉路検出
# 与えられるグラフが負サイクル (辺の重みの総和が負になる有向サイクル) を持つかどうかを判定します。
# 操作回数 O(M) のステップを最大 N 回繰り返すため、時間計算量は O(NM) です。
N,M = map(int, input().split())

E = []
for i in range(M):
    u,v,w = map(int, input().split())
    E.append((u,v,w))

INF = 10**9
dist = [INF]*N
dist[0] = 0

# distの更新
for _ in range(N):
    before = dist.copy()
    for i in range(M):
        u,v,w = E[i]
        dist[v] = min(dist[v], dist[u] + w)

# N回更新後とN-1回更新後の distが変化なしなら, 不サイクルを持たない
print('No' if before==dist else 'Yes')