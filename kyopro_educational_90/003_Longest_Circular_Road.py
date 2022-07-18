from pdb import set_trace as st

N = int(input())
G = [[] for _ in range(N)] #graph
for _ in range(N-1):
    a, b = map(int, input().split())
    #print(a,b)
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

def dfs(s):
    """    depth first search
    """
    dist = [-1] * N
    dist[s] = 0 #頂点sから　各頂点までのパス長さを求める

    st = [s] #stackでDFS
    while st:
        v = st.pop()
        for nv in G[v]: # sとつながっている頂点を順に調べる
            # nv = 隣接頂点
            if dist[nv] == -1:
                st.append(nv)
                dist[nv] = dist[v]+1
    return dist


# 2回やる必要がある
dist0 = dfs(0)
print(dist0)
mv = max(enumerate(dist0), key=lambda x: x[1])[0] #(idx, val) #０から最も遠い頂点番号
print(mv)
distmv = dfs(mv)
print(max(distmv) + 1)