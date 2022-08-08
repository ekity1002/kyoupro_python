N = int(input())
G = [[] for _ in range(N)]

for _ in range(N-1):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

def dfs(s):
    dist = [-1]*N
    dist[s] = 0

    st = [s]
    while st:
        v = st.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v]+1
                st.append(nv)
    return dist

from queue import Queue
def bfs(s):
    dist = [-1]*N
    dist[s] = 0

    que = Queue()
    que.put(s)

    while not que.empty():
        v = que.get()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v]+1
                que.put(nv)
    return dist



ans = 0
for i in range(N):
    #dist = dfs(i)
    dist = bfs(i)
    ans = max(ans, max(dist))
print(ans)