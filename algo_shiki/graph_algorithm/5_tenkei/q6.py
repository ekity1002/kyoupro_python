import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int, input().split())
    G[a].append(b)

# ならべかえ
for i in range(N):
    G[i].sort()

seen = [-1] * N
ans = []

def rec(v):
    seen[v] = 1
    for nv in G[v]:
        if seen[nv] != -1:
            continue
        rec(nv)
    ans.append(v)    

for v in range(N):
    if seen[v] != -1:
        continue
    rec(v)

ans = ans[::-1]
print(*ans)
