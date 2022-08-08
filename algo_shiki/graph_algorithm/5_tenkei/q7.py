from queue import Queue

N, M = map(int, input().split())
G = [[] for _ in range(N)]
deg = [0] * N

for i in range(M):
    a,b = map(int, input().split())
    G[b].append(a) #G[i]:  iへ接続している頂点番号
    deg[a]+=1

# 出自数(頂点nから出ている辺の数)
for i in range(N):
    G[i].sort()

#print(G)
que = Queue()
for v in range(N):
    if deg[v]==0:
        que.put(v)

ans = []
while not que.empty():
    v = que.get()
    ans.append(v)
    for nv in G[v]:
        deg[nv] -= 1
        if deg[nv] == 0:
            que.put(nv)
ans = ans[::-1]
print(*ans)