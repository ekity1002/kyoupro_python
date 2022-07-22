N,M,s,t = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)

def bfs(s):
    """深さ優先検索
    s:始点の番号
    """
    dist = [(-1,-1,-1)] * N
    dist[s] = (s,0,-1) #現在の頂点, 開始からの距離, 一つ前の頂点

    st = [s]
    while st:
        v = st.pop()
        for nv in G[v]:
            if dist[nv][1] == -1:
                dist[nv] = (nv, dist[v][1]+1, v)
                st.append(nv)
    return dist

dist = bfs(s)
#print(dist)
#dist.sort(key=lambda x: x[1])
#print(dist)
cnt = 0
ans = []
cnt+=1
ans.append(t)

nv = dist[t][2]
while True:
    #print(nv, ans)
    cnt+=1
    ans.append(nv)
    nv = dist[nv][2]
    if nv == -1:
        break
print(cnt)
print(*ans[::-1])