# デッドロック
from queue import Queue

# 四方向への移動を表すベクトル
# 0: 下、1: 右、2: 上、3: 左
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

# 入力
N, M = map(int, input().split())
G = [[] for _ in range(N)]
deg = [0]*N #拡張店の出自数を管理する

for _ in range(M):
    f, s = map(int, input().split())
    #G[s].append(f)
    G[f].append(s)
    deg[s] += 1


que = Queue()

num = 0 # 除去された頂点の個数
for v in range(N):
    if deg[v] == 0:
        # ソースの頂点をqueに入れる
        que.put(v)
        num += 1

while not que.empty():
    # キューから頂点を取り出す
    v = que.get()

    for v2 in G[v]:
        deg[v2] -= 1

        if deg[v2] == 0:
            que.put(v2)
            num += 1


        
print("Yes" if num == N else "No")