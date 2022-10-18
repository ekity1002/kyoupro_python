# D - LRUD Instructions
from collections import defaultdict

H, W, rs, cs = map(int, input().split())
N = int(input())

wall = defaultdict(int)  # 壁情報

w_list = [[0] for _ in range(N)]  # 横壁 index list
h_list = [[0] for _ in range(N)]  # 立壁 index list

for i in range(N):
    r, c = map(int, input().split())
    wall[(r, c)] = 1
    w_list[r].append(c)
    h_list[c].append(r)

w_list.append(W + 1)
h_list.append(H + 1)

Q = int(input())
current = (rs, cs)


def move(current, d):
    r, c = current
    if d == "L":
        new_current = (r, c - 1)
    elif d == "R":
        new_current = (r, c + 1)
    elif d == "U":
        new_current = (r - 1, c)
    elif d == "D":
        new_current = (r + 1, c)

    is_wall = wall[new_current]
    if is_wall:
        return current

    # はみ出していないか
    if 1 <= new_current[0] <= H and 1 <= new_current[1] <= W:
        return new_current

    return current


ans = []
for _ in range(Q):
    d, l = input().split()
    l = int(l)

    # 動かす方向を見る
    # その方向の壁の indexを取得
    # L or R: H[] から bisect_left でcurrent の c がはいる index
    # U or D W[] から bisect_left でcurrent の r がはいる index
    # index 1以上 H以下 壁の一つ手前の座標に更新
    # 最も近い壁 の 座標取得
    # もっとも 近い壁の手前に current を更新
    for i in range(l):
        new_current = move(current, d)
        if current == new_current:
            break
        current = new_current
    # マスを出力
    print(*current)
    # ans.append(current)

# [print(*a) for a in ans]
