N, M = map(int, input().split())
G = [[] for _ in range(N)]

for i in range(M):
    u, v, w = map(int, input().split())
    G[u].append((v,w))

#print(G)
INF=100000000000000
def dfs(s):
    dist = [INF] * N
    dist[s] = 0

    st = [s]
    while st:
        v = st.pop()
        for nv, d in G[v]:
            if dist[nv] > (dist[v] + d):
                dist[nv] = min(dist[nv], dist[v] + d)
                st.append(nv)
    return dist

dist = dfs(0)
print(dist[-1] if dist[-1] != INF else -1)