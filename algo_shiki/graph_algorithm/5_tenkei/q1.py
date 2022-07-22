N,M,s,t = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)

def dfs(s):
    dist = [-1] * N
    dist[s] = 0

    st = [s]
    while st:
        v = st.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                st.append(nv)
    return dist


dist = dfs(s)
if dist[t] == -1:
    print('No')
else:
    print('Yes')