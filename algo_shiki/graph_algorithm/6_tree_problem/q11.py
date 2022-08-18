from collections import deque

# BFS ライクに頂点を見ていく関数
def bfs(children, par, W, dp1, dp2):
    leaf = deque([])    # 探索すべき頂点を入れるキュー (最初は葉をいれる)
    # 自分の子頂点がすべて探索されたかチェックするための配列を作る
    deg = [0 for _ in range(N)] # deg[i]：頂点 i の子頂点数
    for v in range(N):
        deg[v] = len(children[v])
        if deg[v] == 0: leaf.append(v)
    
    # 葉が残っている限り
    while len(leaf):
        v = leaf.popleft()
        ans1 = W[v] # dp1[v] (頂点 v を含む安定集合のうち、重みの最大値) の答えとなる変数 
        ans2 = 0    # dp2[v] (頂点 v を含まない安定集合のうち、重みの最大値) の答えとなる変数

        for nv in children[v]:
            # 頂点 v を選ぶ場合、子頂点を選ぶことはない
            ans1 += dp2[nv]
            # 頂点 v を選ばない場合、子頂点を選んでも選ばなくても良い
            ans2 += max(dp1[nv], dp2[nv])
        
        # DP テーブルを埋める
        dp1[v] = ans1
        dp2[v] = ans2

        # 頂点 v の親頂点 p について、deg[p] を 1 減らす
        # p の子頂点たちがすべてチェックされた (deg[p] == 0) となったら、p もキューに入れる
        p = par[v]
        deg[p] -= 1
        if deg[p] == 0:
            leaf.append(p)

    return


# main
# 入力の受け取り
N = int(input())
G = [[] for _ in range(N)]    # グラフを表現する隣接リスト
for i in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
W = list(map(int, input().split()))

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

# キューが空になるまで、探索を続ける
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

dp1 = [0 for _ in range(N)] # dp1[v]：頂点 v を根とする部分木について、頂点 v を含む安定集合のうち、重みの最大値
dp2 = [0 for _ in range(N)] # dp2[v]：頂点 v を根とする部分木について、頂点 v を含まない安定集合のうち、重みの最大値
# 探索を開始する
bfs(children, par, W, dp1, dp2)

# dp1[r], dp2[r] の最大値が答え
ans = max(dp1[r], dp2[r])
print(ans)