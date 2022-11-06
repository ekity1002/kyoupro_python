# 二部グラフ判定 (木 ver.)
# 白はしろと隣り合わない、黒は黒と隣り合わない
# 木は常に2部グラフ
from collections import deque

N = int(input())
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[b].append(a)
    G[a].append(b)


color = [-1 for _ in range(N)]  # vが黒なら1, 白なら0
ans = "Yes"
for v in range(N):
    if color[v] != -1:
        continue

    deq = deque([])
    color[v] = 0
    deq.append(v)
    while len(deq) > 0:
        qv = deq.popleft()

        for nv in G[qv]:
            if color[nv] != -1:
                if color[nv] == color[qv]:
                    ans = "No"
                continue

            # nv の色をqvと逆にしてセット
            color[nv] = 1 - color[qv]
            deq.append(qv)
print(ans)
