# Q9. 木の最小点被覆
N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# 一つの頂点しかつながっていない場所をのぞく
from collections import deque
r = 0
parents = [-1]*N
children = [[] for _ in range(N)]
seen = [False]*N
que = deque([])

que.append(r)
seen[r]=True
while len(que):
    v = que.popleft()
    for nv in G[v]:
        if seen[nv]: continue
        seen[nv]=True
        parents[nv]=v
        children[v].append(nv)
        que.append(nv)

def bfs(children, parents, ischosen):
    leaf = deque([])
    deg = [0 for _ in range(N)]
    for v in range(N):
        deg[v] = len(children[v])
        if deg[v] == 0: leaf.append(v)

    # 一番下の葉から探索
    while len(leaf):
        v = leaf.popleft()
        cnt = 0
        for nv in children[v]:
            # 子供が選ばれているなら cnt
            if not ischosen[nv]: cnt += 1
        
        if cnt >= 1: ischosen[v] = True

        p = parents[v]
        if p == -1: continue

        deg[p] -= 1
        if deg[p] == 0:
            # pの子がすべてチェックされたら親を追加
            leaf.append(p)

    return



ischosen = [False for _ in range(N)]
bfs(children, parents, ischosen)

# 選ばれている頂点数が答え
ans = 0
for v in range(N):
    if ischosen[v]: ans += 1
print(ans)