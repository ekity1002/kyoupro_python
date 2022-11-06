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


N, M = map(int, input().split())
E = [[] for _ in range(M)]
for i in range(M):
    u, v, w = map(int, input().split())
    E[i] = (u, v, w)

E.sort(key=lambda x: x[2])

uf = UnionFind(N)
W = 0
for i in range(M):
    u, v, w = E[i]
    if uf.issame(u, v):
        continue

    uf.unite(u, v)
    W += w

ans = 0
for i in range(M):
    w_sub = 0
    uf_sub = UnionFind(N)
    for j in range(M):
        if i == j:
            continue

        u, v, w = E[j]
        if uf_sub.issame(u, v):
            continue

        uf_sub.unite(u, v)
        w_sub += w

    if uf_sub.size(0) < N or w_sub > W:
        ans += 1

print(ans)
