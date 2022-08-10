# Q7. 木の最大安定集合
# https://algo-method.com/tasks/978
from collections import deque

def bfs(children, par, ischosen):
    leaf = deque([]) #探索すべき頂点のキュー
    deg = [0 for _ in range(N)] # 頂点i の子頂点数

    for v in range(N):
        deg[v] = len(children[v])
        if deg[v] == 0: leaf.append(v)

    while len(leaf):
        v = leaf.popleft()
        flg = False #vの子頂点がすでに選ばれているか

        for nv in children[v]:
            flg |= ischosen[nv] #子張点が選ばれていれば flg を true にする

        # 子頂点が一つも選ばれていない場合のみ v を選ぶ
        ischosen[v] = not flg

        # 頂点 v の親頂点 p について、deg[p] を 1 減らす
        # p の子頂点たちがすべてチェックされた (deg[p] == 0) となったら、p もキューに入れる
        p = par[v]
        deg[p] -= 1
        if deg[p] == 0:
            leaf.append(p)
        

N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


r =0 #根とする頂点番号
children = [[] for _ in range(N)] #ある頂点の小頂点
par = [-1 for _ in range(N)] #頂点i の親頂点番号
seen = [False for _ in range(N)]
que = deque([]) #調べる頂点管理するキュー

# 根の登録
seen[r] = True
par[r] = r
que.append(r)

while len(que) > 0:
    v = que.popleft()

    for nv in G[v]:
        if seen[nv]: continue

        seen[nv]=True
        children[v].append(nv)
        par[nv] = v
        que.append(nv)

ischosen = [False for _ in range(N)]
bfs(children, par, ischosen)

# 選ばれた頂点数が答え
ans = 0
for v in range(N):
    if ischosen[v]: ans += 1
print(ans)
