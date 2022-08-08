N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int ,input().split())
    G[a].append(b)
    G[b].append(a)

def dfs(s):
    dist = [-1] * N
    dist[s] = 0
    
    st = [s]
    while st:
        v = st.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v]+1
                st.append(nv)
    return dist

from pdb import set_trace as st
from queue import Queue
def bfs(s):
    #n_nodes = [len(G[i]) for i in range(N)]
    dist = [-1] * N
    dist[s] = 0

    que = Queue()
    que.put(s)
    #st()
    while not que.empty():
        v = que.get()
        #print(v)
        for nv in G[v]:
            #n_nodes[v] -= 1
            if dist[nv] == -1:
                dist[nv] = dist[v]+1
                que.put(nv)
    return dist


#dist = dfs(0)
dist = bfs(0)
#print(dist)
print(max(dist))

