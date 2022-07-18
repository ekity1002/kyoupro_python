N, M = map(int, input().split())
G = [[] for _ in range(N)]
#seen = [False for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1] * N
nodes = [[] for _ in range(N)]
dist[0] = 0
nodes[0] = [0]

for k in range(1, N):
    for v in nodes[k-1]:
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v]+1
            nodes[k].append(nv)
#print(dist)
print(max(dist))