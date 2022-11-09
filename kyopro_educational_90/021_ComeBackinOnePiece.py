# グラフ
# SCC 強連結成分分解

N, M = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(M)]
print(S)
# 有向グラフの典型入力を双方向で適用
from collections import defaultdict

adj, adj_inv = defaultdict(list), defaultdict(list)
for a, b in S:
    adj[a - 1].append(b - 1)
    adj_inv[b - 1].append(a - 1)

# Step1: 帰りがけ順（backword_listを作る）

seen = [False] * N
finished = [False] * N
backward_list = []


def dfs1(pos):
    todo = []
    todo.append(pos)  # 初期探索場所をpush
    while todo:
        pos = todo.pop()  # LIFOでpop
        if finished[pos]:
            continue
        seen[pos] = True
        # 帰りがけの判定
        next_list = [x for x in adj[pos] if not seen[x]]
        if len(next_list) == 0:
            finished[pos] = True
            backward_list.append(pos)
        else:
            todo.append(pos)
            for next_ in next_list:
                todo.append(next_)
    return


for n in range(N):
    if not seen[n]:
        dfs1(n)

# Step2: 帰りがけの逆順でdfsすることでグループを求める

seen = [False] * N
groups = defaultdict(list)


def dfs2(pos, label):
    todo = []
    todo.append(pos)  # 初期探索場所をpush
    while todo:
        pos = todo.pop()  # LIFOでpop
        if seen[pos]:
            continue
        seen[pos] = True
        groups[label].append(pos)
        # 次の位置を探索する
        for next_ in adj_inv[pos]:
            todo.append(next_)
    return


ans = 0
label = 0
for n in reversed(backward_list):  # 帰りがけの逆順
    if not seen[n]:
        dfs2(n, label)
        label += 1

for k, v in groups.items():
    num = len(v)
    ans += num * (num - 1) // 2
print(ans)
