from queue import Queue
N,M,s,t = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)


dist = [(-1,-1,-1)] * N
dist[s] = (s, 0, 0)

que = Queue()
que.put(s)

while not que.empty():
    v = que.get()
    for nv in G[v]:
        if dist[nv][1] == -1:
            dist[nv] = (nv, dist[v][1] + 1, v)
            que.put(nv)

print(dist[t][1]+1) #パスに含まれる超点数 = 距離+1
ans = []
#print(dist)
pn = t
ans.append(pn)
while True:
    pn = dist[pn][2] #一つ前のノード番号
    ans.append(pn)
    if pn == s:
        break
print(*ans[::-1],)