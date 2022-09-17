# 8. 最長路問題
# 最短経路の改変
N,M = map(int, input().split())
E = []
for i in range(M):
    u,v,w = map(int, input().split())
    E.append((u,v,w))

# 初期値を-INFにしておく.
INF = 10**9
dist = [-INF]*N
dist[0] = 0

# ベルマンフォード法. N回繰り返すと収束する
for k in range(N):
    for i in range(M):
        u,v,w = E[i]
        
        if dist[u] + w > dist[v] and dist[u] != -INF:
            dist[v] = dist[u]+w

ans = dist[N-1]
print(ans)