from queue import Queue
N, M = map(int, input().split())
G = [[] for _ in range(N)]
#seen = [False for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1] * N
nodes = [[] for _ in range(N)] #que の代わりに使える
dist[0] = 0
nodes[0] = [0]
que = Queue()
que.put(0)

# while not que.empty():
#     v  = que.get()
#     for nv in G[v]:
#         if dist[nv] == -1:
#             dist[nv] = dist[v]+1
#             que.put(nv)

for k in range(1,N):
    for v in nodes[k-1]:
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v]+1
                nodes[k].append(nv)

            
print(max(dist))