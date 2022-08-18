from collections import deque
MOD = 998244353

N = int(input())
G = [[] for _ in range(N)]    # グラフを表現する隣接リスト
for i in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


# グラフを根付き木に変える
# 頂点 0 を根とする
r = 0
# 根を始点として幅優先探索を行う
children = [[] for _ in range(N)]   # children[i]：頂点 i の子頂点たちを格納する配列
par = [-1 for _ in range(N)]    # par[i]：頂点 i の親頂点番号
seen = [False for _ in range(N)]    # seen[i]：頂点 i を探索済みか
que = deque([]) # これから調べるべき頂点を管理するキュー
# 根を始点として登録する
seen[r] = True
par[r] = r
que.append(r)

while len(que) > 0:
    # 次に調べるべき頂点を v とする
    v = que.popleft()

    # 頂点 v に隣接する頂点 nv について、
    for nv in G[v]:
        # 頂点 nv が探索済みならば、スキップする
        if seen[nv]: continue
        # そうでないならば、children などの情報を更新してキューに nv を挿入する
        seen[nv] = True
        children[v].append(nv)
        par[nv] = v
        que.append(nv)

def bfs(children, par, dp1, dp2):
    deg = [0]*N
    leaf = deque([])
    for v in range(N):
        deg[v] = len(children[v])
        if deg[v]==0:
            leaf.append(v)

    while len(leaf) > 0:
        v = leaf.popleft()

        ans1 = 1
        ans2 = 1
        for nv in children[v]:
            # 掛け算した後のあまりと、個別の数のあまりの掛け算の結果は同じ？？
            ans1 *= dp2[nv]
            ans1 %= MOD
            ans2 *= (dp1[nv] + dp2[nv])
            ans2 %= MOD

        dp1[v] = ans1
        dp2[v] = ans2

        p = par[v]
        deg[p] -= 1
        if deg[p] == 0:
            leaf.append(p)
        

dp1 = [0 for _ in range(N)] # dp1[v]：頂点 v を根とする部分木について、頂点 v を含む安定集合のうち、重みの最大値
dp2 = [0 for _ in range(N)] # dp2[v]：頂点 v を根とする部分木について、頂点 v を含まない安定集合のうち、重みの最大値

# 探索を開始する
bfs(children, par, dp1, dp2)
print((dp1[r] + dp2[r]) % MOD)