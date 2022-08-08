import sys
sys.setrecursionlimit(10**6)
from queue import Queue

# 頂点 v を始点とした深さ優先探索
def bfs(s, G, color):
    que = Queue()
    que.put(s)
    while not que.empty():
        v = que.get()
        for nv in G[v]:
            if color[nv] == -1:
                color[nv] = 1 - color[v]
                que.put(nv)
            if color[nv] == color[v]:
                return False
    return True
    

# main
# 入力を受け取る
N, M = map(int, input().split())
G = [[] for _ in range(N)]  # グラフを表現する隣接リスト
for i in range(M):
    a, b = map(int, input().split())
    # 頂点 a から頂点 b への辺を張る
    G[a].append(b)
    # 無向グラフのため、頂点 b から頂点 a への辺も張る
    G[b].append(a)

color = [-1 for _ in range(N)]    # color[v]：頂点 v の色が黒なら 1, 白なら 0, 未探索なら -1
ans = 'Yes'

# 全ての頂点について
for v in range(N):
    # 頂点 v がすでに訪問済みであれば、スキップ
    if color[v] != -1: continue
    # そうでなければ、頂点 v を含む連結成分は未探索
    # 頂点 v の色を白で決め打ちしたうえで、深さ優先探索を行う
    color[v] = 1
    if not bfs(v, G, color): ans = 'No'
# 答えを出力する
print(ans)