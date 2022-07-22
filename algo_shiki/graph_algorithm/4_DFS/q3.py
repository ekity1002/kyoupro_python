N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

def dfs(s):
    dists = [-1] * N
    dists[s] = 0
    print(s)

    st = [s]
    while st:
        v = st.pop() #
        for nv in G[v]: #vに隣接する頂点番号
            if dists[nv] == -1 :
                st.append(nv)
                #print(nv)
                dists[nv] = dists[v]+1
    return dists

print(dfs(0))
