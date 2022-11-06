# D - LRUD Instructions
from collections import defaultdict

from bisect import bisect_left

H, W, rs, cs = map(int, input().split())
N = int(input())

wall = defaultdict(int)  # 壁情報

w_list = defaultdict(lambda: [0])  # 横壁 index list
h_list = defaultdict(lambda: [0])  # 横壁 index list

for i in range(N):
    r, c = map(int, input().split())
    wall[(r, c)] = 1
    w_list[r].append(c)
    h_list[c].append(r)

for k, v in w_list.items():
    w_list[k].append(W + 1)
    w_list[k].sort()
for k, v in h_list.items():
    h_list[k].append(H + 1)
    h_list[k].sort()

print(w_list)
Q = int(input())
current = (rs, cs)

from pdb import set_trace as st


def move(current, d, l):
    # 動かす方向を見る
    # その方向の壁の indexを取得
    r, c = current
    st()
    if d == "L":
        idx = bisect_left(
            w_list[r],
            c,
        )
        # 壁の座標
        if idx == 0:
            wall_c = 0
        else:
            wall_c = w_list[r][idx]

        if c - l <= wall_c:
            # 途中で壁に当たる場合、壁の手前の座標
            new_current = (r, wall_c + 1)
        else:
            new_current = (r, c - l)
    elif d == "R":
        idx = bisect_left(
            w_list[r],
            c,
        )
        # 壁の座標
        if idx == 0:
            wall_c = W + 1
        else:
            wall_c = w_list[r][idx]
        if c + l >= wall_c:
            # 途中で壁に当たる場合、壁の手前の座標
            new_current = (r, wall_c - 1)
        else:
            new_current = (r, c + l)
    elif d == "U":
        idx = bisect_left(
            h_list[c],
            r,
        )
        # 壁の座標
        if idx == 0:
            wall_r = 0
        else:
            wall_r = h_list[c][idx]

        if r - l <= wall_r:
            # 途中で壁に当たる場合、壁の手前の座標
            new_current = (wall_r + 1, c)
        else:
            new_current = (r - l, c)
    elif d == "D":
        idx = bisect_left(
            h_list[c],
            r,
        )
        # 壁の座標
        if idx == 0:
            wall_r = H + 1
        else:
            wall_r = h_list[c][idx]

        # 壁の座標
        wall_r, wall_c = h_list[c][idx], w_list[r][c]
        if r + l >= wall_r:
            # 途中で壁に当たる場合、壁の手前の座標
            new_current = (wall_r - 1, c)
        else:
            new_current = (r + l, c)

    return new_current


ans = []
for _ in range(Q):
    d, l = input().split()
    l = int(l)

    new_current = move(current, d, l)
    # マスを出力
    # print(*current)
    ans.append(new_current)

[print(*a) for a in ans]
