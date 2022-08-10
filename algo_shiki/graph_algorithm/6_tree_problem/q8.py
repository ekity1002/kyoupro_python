N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


def bfs(children, parent, ismatched):
    leaf = deque([]) #探索キュー
    deg = [0 for _ in range(N)] #頂点iの小頂点数
    for v in range(N):
        deg[v] = len(children[v])
        if deg[v]==0: leaf.append(v) #葉の頂点をleafに加える

    while len(leaf):
        v = leaf.popleft()

        p = parent[v]
        if p == -1: continue #vがrootならなにもしない

        # vとp がマッチングしていなければマッチング
        if not ismatched[v] and not ismatched[p]:
            ismatched[v] = ismatched[p] = True

        deg[p] -= 1
        if deg[p]==0:
            leaf.append(p)


from collections import deque #両端以外のアクセスは list の方が良い
r=0 #root
children = [[] for _ in range(N)]
parent = [-1 for _ in range(N)]
seen = [False for _ in range(N)]
que = deque([])

seen[r]=True
que.append(r)

while len(que)>0:
    v = que.popleft() #先頭から要素を一つ削除
    for nv in G[v]:
        if seen[nv]: continue
        seen[nv]=True
        children[v].append(nv) #
        parent[nv]=v
        que.append(nv)

ismatched = [False for _ in range(N)]
bfs(children, parent, ismatched)

ans = 0
for v in range(N):
    if ismatched[v]: ans+=1

ans //= 2
print(ans)