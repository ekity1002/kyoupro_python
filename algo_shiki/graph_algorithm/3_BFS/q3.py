from queue import Queue

# 四方向への移動を表すベクトル
# 0: 下、1: 右、2: 上、3: 左
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

# 入力
H, W = map(int, input().split())
X0, Y0, X1, Y1 = map(int, input().split())
S = [input() for i in range(H)]

# 各マス (x, y) が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [[-1] * W for i in range(H)]

# todo リストを表すキュー
que = Queue()

# マス (X0, Y0) を始点とする
dist[X0][Y0] = 0
que.put((X0, Y0))
#print(S)
while not que.empty():
    # キューから頂点を取り出す
    x, y = que.get()

    # マス (x, y) から 1 手で行けるマスを順に探索
    for dx, dy in zip(dxs, dys):
        # 隣接マス
        x2, y2 = x + dx, y + dy

        # マス (x2, y2) が盤面外である場合、黒マスである場合はスキップ
        if x2 < 0 or x2 >= H or y2 < 0 or y2 >= W or S[x2][y2] == 'B':
            continue
        
        # マス (x2, y2) が探索済みであれば何もしない
        if dist[x2][y2] != -1:
            continue

        # マス (x2, y2) を探索する
        dist[x2][y2] = dist[x][y] + 1
        que.put((x2, y2))
        
# マス (X1, Y1) の値を答える
print(dist[X1][Y1])