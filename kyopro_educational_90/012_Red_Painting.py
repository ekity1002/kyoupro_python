# UNION FIND を使う
# https://algo-method.com/descriptions/136

H, W = map(int, input().split())
Q = int(input())

queries = []
for i in range(Q):
    queries.append(list(map(int, input().split())))


class UnionFind():
    def __init__(self,n):
        """n: 頂点数"""
        self.par = [-1]*n
        self.rank = [0]*n
        self.siz = [1]*n


    def root(self, x):
        """rootを求める"""
        # xが root の場合は xを返す
        if self.par[x] == -1: return x
        else:
            #経路圧縮: 何度も再起しなくてよいようにする
            self.par[x] = self.root(self.par[x]) 
            return self.par[x]

    def issame(self, x, y):
        """x,yが同じグループに属するか（rootが一致するか)"""
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        """xを含むグループと yを含むグループを併合する
        つながっているかどうか を求めるための構造。、距離はどうでも良い
        そのため、２つのグループを併合している

        """
        # xとyのrootを取得する
        rx = self.root(x)
        ry = self.root(y)

        if rx==ry: return False #すでに同じグループのときはなにもしない

        # union by rank
        # 木の深さが深くならないようにする工夫。
        # 深さが大きい方に、小さい方をつなげるほうが全体の深さが小さくなる。
        if self.rank[rx] < self.rank[ry]:
            # ry側のrankが小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx #rxの子とする
        if self.rank[rx] == self.rank[ry]:
            # rxがわのrankを調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] #rx側の sizを調整する
        return True

    def size(self, x):
        """xを含む根付き木のサイズを求める"""
        return self.siz[self.root(x)]

uf = UnionFind(H*W)
B = [[False]*W  for _ in range(H)]


def check(r,c):
    """r,cの上下に赤ますがあるか"""
    if 1 <= r: #ue
        if B[r-1][c]: uf.unite(r*W + c, (r-1)*W + c)
    if r < H-1: #shita
        if B[r+1][c]: uf.unite(r*W + c, (r+1)*W + c)
    if 1 <= c: #hidari
        if B[r][c-1]: uf.unite(r*W + c, r*W + c-1)
    if c < W-1 : #migi
        if B[r][c+1]: uf.unite(r*W + c, r*W + c+1)


is_painted = False
for q in queries:
    if len(q) == 3:
        _, r, c = q
        B[r-1][c-1]=True
        check(r-1, c-1)
        is_painted = True
    else:
        _, ra, ca, rb, cb = q
        ra,ca,rb,cb = ra-1, ca-1, rb-1, cb-1
        x = ra*W + ca
        y = rb*W + cb
        if is_painted:
            print('Yes' if B[ra][ca] and B[rb][cb] and uf.issame(x,y)  else 'No')
        else:
            print('No')


