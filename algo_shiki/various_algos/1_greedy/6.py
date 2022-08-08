# 入力
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

# 二頂点間の距離を求める関数
def calc(i, j):
    return ((XY[j][0]-XY[i][0])**2 + (XY[j][1]-XY[i][1])**2) ** 0.5

# 答え
res = 0

# すでに訪れた頂点を set 型で管理
visited = set()
visited.add(0)

# 前回の頂点
prev = 0

from pdb import set_trace as st
# 毎回貪欲に頂点を選んでいく
st()
for i in range(N - 1):
    # 残っている頂点で最も近いところを探す
    # tuple の list に minをかける。 (距離、頂点番号) がはいっていて、前の要素から評価される
    min_dis, nex = min([(calc(prev, j), j) for j in range(N) if j not in visited])

    # 新たに頂点 nex を訪れる
    visited.add(nex)
    res += min_dis

    # 前回頂点を更新
    prev = nex

# 最後に頂点 0 へ戻る
res += calc(prev, 0)

# 出力
print(res)