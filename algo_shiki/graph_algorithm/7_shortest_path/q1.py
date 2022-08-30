# DAGの最短路
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dist = [-1] * N

for v in range(N):
    if v==0:
        dist[v]=0
    elif v==1:
        dist[v] = dist[v-1]+A[v-1]
    else:
        dist[v] = min(dist[v-1]+A[v-1], dist[v-2]+B[v-2])

print(dist[N-1])