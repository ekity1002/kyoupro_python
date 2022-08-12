N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

from collections import deque
r = 0
parent = [-1]*N
children = [[] for _ in range(N)]
seen =  [False]*N

seen[r]=True
que = deque([])
que.append(r)

while len(que):
    v = que.popleft()
    for nv in G[v]:
        if seen[nv]: continue
        seen[nv]=True
        parent[nv] = v
        children[v].append(nv)
        que.append(nv)


def bfs(children, parent, iscovered):
    edge_num=0 #選んだ辺の数
    leaf = deque([])
    deg = [0]*N
    for v in range(N):
        deg[v] = len(children[v])
        if deg[v]==0: leaf.append(v)
    #from pdb import set_trace as st
    #st()
    while len(leaf):
        v = leaf.popleft()
        p = parent[v]

        if not iscovered[v]:
            iscovered[v] = iscovered[p] = True
            edge_num+=1
        
        deg[p] -= 1
        if deg[p] == 0:
            leaf.append(p)

    return edge_num

#print(children, parent)
iscovered = [False]*N #頂点N が辺によってカバーされている
ans = bfs(children, parent, iscovered)
print(ans)