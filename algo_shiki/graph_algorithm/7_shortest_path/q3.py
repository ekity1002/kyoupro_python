N, M = map(int, input().split())
G = [[] for _ in range(N)]

for i in range(M):
    u, v, w = map(int, input().split())
    G[u].append((v,w))

#print(G)
INF=100000000000000
ans = []

for v in range(N):
    dist = INF
    ans_v = -1
    for nv, d in G[v]:
        if dist > d:
            dist = d
            ans_v = nv
        if dist == d:
            ans_v = min(ans_v, nv)
    print(ans_v)
    # ans.append(ans_v)
