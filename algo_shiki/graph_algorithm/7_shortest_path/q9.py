# Q9. 経路復元
# 最短経路を求め、パスを出力する
N,M = map(int, input().split())
E = []
G = [[] for i in range(N)]
for i in range(M):
    u,v,w = map(int, input().split())
    E.append((u,v,w))
    G[u].append((v,w))


INF = 10**9
dist = [INF]*N
dist[0] = 0
prev = [-1]*N  #頂点i の前にどこにいたか

for k in range(N):
    for i in range(M):
        u,v,w = E[i]

        # minを使うと更新されたかわからないのでこうする
        if dist[u]+w < dist[v] and dist[u] != INF:
            dist[v] = dist[u]+w
            prev[v] = u

s = N-1
ans = [s]
while 1:
    s = prev[s]
    ans.append(s)
    if s==0:
        break
print(len(ans))
print(*ans[::-1], sep=" ")