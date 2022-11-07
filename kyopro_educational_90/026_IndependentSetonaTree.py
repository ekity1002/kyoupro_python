# ２部グラフの性質
N = int(input())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

from pdb import set_trace


def dfs(s):
    cur = 0
    col = [-1] * N
    col[s] = cur

    st = [s]
    # set_trace()
    while st:
        # print(st)
        v = st.pop()
        cur = col[v]
        for nv in G[v]:
            if col[nv] == -1:
                st.append(nv)
                col[nv] = 1 - cur
    return col


s = 0
col = dfs(s)
# print(G)
# print("col", col)
ans1 = []
ans2 = []
for i in range(N):
    if col[i]:
        ans1.append(i + 1)
    else:
        ans2.append(i + 1)
    if len(ans1) >= N // 2:
        print(*ans1)
        break
    if len(ans2) >= N // 2:
        print(*ans2)
        break
