# 辺情報を表す構造体
class edge:
    def __init__(self, start, end, leng):
        self.start = start  # 辺の始点
        self.end = end      # 辺の終点
        self.leng = leng    # 辺の重み

INF = 10**9 # 初期化で使う十分大きな数

# main
# 入力を受け取る
N, M = map(int, input().split())
graph_edges = [[] for _ in range(M)]    # graph_edges[i]：i 番目の辺情報
for i in range(M):
    u, v, w = map(int, input().split())
    graph_edges[i] = [u, v, w]

dist = [INF for _ in range(N)]  # dist[i]：現在の d_i の値 (0 以外は 10^9 で初期化する)
# d_0 を 0 で初期化する
dist[0] = 0

# i = 0, 1, …, M-1 の順に、辺 i への操作を行う
for i in range(M):
    # i 番目の辺の始点、終点、重みをそれぞれ u, v, w とおく
    u, v, w = graph_edges[i]
    # dist[v] を置き換える
    dist[v] = min(dist[v], dist[u] + w)

# 答えを出力する
for v in range(N):
    print(dist[v])