N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

seen = [0]*N
def dfs(s):
    dist = [-1]*N
    dist[s]=0

    st = [s]
    while st:
        v = st.pop()
        seen[v] = 1
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v]+1
                st.append(nv)
            
    return dist


# def bfs(s):
#     n

ans = 0
for i in range(N):
    if seen[i]:
        continue
    dist = dfs(i)
    edge = dist.index(max(dist))
    dist2 = dfs(edge)
    ans = max(ans, max(dist2))
print(ans)