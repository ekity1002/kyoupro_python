N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

def dfs(s):
    dist = [-1] * N
    dist[s] = 0

    st = [s]
    while st:
        v = st.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                st.append(nv)
                dist[nv] = dist[v]+1
    return dist

dists = dfs(0)
ans = 0
for i in dists:
    if i < 0:
        ans+=1
print(ans)