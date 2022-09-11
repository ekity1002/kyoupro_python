N, M = map(int, input().split())
E = []
for i in range(M):
    u,v,w = map(int, input().split())
    E.append([u,v,w])

INF = 10**9
dist = [INF]*N
dist[0] = 0
#print(E)
def step():
    for i in range(M):
        u,v,w = E[i]
        dist[v] = min(dist[v], dist[u]+w)

K = 1
while 1:
    before = dist.copy()
    step()
    if before == dist:
        break
    K+=1
print(K)