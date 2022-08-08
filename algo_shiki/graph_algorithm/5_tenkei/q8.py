#サイクル検出
import sys
sys.setrecursionlimit(10**6)


N,M = map(int, input().split())
G = [[] for _ in range(N)]
seen = [0] * N
flg = False
finished = [False] * N
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)


def rec(v):
    global flg
    seen[v] = 1
    for nv in G[v]: #0につながる点
        if seen[nv] == 1: #0につながっているところをすでに三鷹
            if finished[nv] == False: #戻ってきてしまった場合
                flg = True
            continue
        rec(nv)
    finished[v] = True #一番奥の点まで見たら終了フラグつける

for v in range(N):
    if seen[v] == 1:
        continue
    rec(v)

if flg:
    print('Yes')
else:
    print('No')