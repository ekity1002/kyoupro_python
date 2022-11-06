# Q6. グリッドグラフ

# Union-Find
class UnionFind:
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        for i in range(n):
            self.par[i] = i
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == x:
            return x  # x が根の場合は x を返す
        else:
            self.par[x] = self.root(self.par[x])  # 経路圧縮
            return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False  # すでに同じグループのときは何もしない
        # union by size
        if self.siz[rx] > self.siz[ry]:  # ry 側の siz が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx  # ry を rx の子とする
        self.siz[rx] += self.siz[ry]  # rx 側の siz を調整する
        return True

    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]


def edge_num(i, j):
    # 頂点 (i, j) を 0 以上 HW 未満の整数に変換する
    return i * W + j


# 平面は (H−1)(W−1)+1 個の領域に分かれています (外側の領域も含む)。
H, W = map(int, input().split())
A = []
B = []
for i in range(H):
    A.append(list(map(int, input().split())))
for i in range(H - 1):
    B.append(list(map(int, input().split())))

# 頂点数、辺数
N = H * W
M = H * (W - 1) + W * (H - 1)

# 辺情報の作成
sum_weight = 0
E = []  # 辺情報 (開始頂点, 終了頂点, 辺重み)
for i in range(H):
    for j in range(W - 1):
        u, v = edge_num(i, j), edge_num(i, j + 1)
        w = A[i][j]
        E.append((u, v, w))
        sum_weight += w

for i in range(W):
    for j in range(H - 1):
        u, v = edge_num(j, i), edge_num(j + 1, i)
        w = B[j][i]
        E.append((u, v, w))
        sum_weight += w

# 降順にソート
E.sort(key=lambda x: x[2], reverse=True)
uf = UnionFind(N)

ans = sum_weight
for i in range(M):
    u, v, w = E[i]
    if uf.issame(u, v):
        continue

    uf.unite(u, v)

    ans -= w

print(ans)
