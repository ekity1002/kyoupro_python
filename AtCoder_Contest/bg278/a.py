N, K = map(int, input().split())
A = list(map(int, input().split()))
for i in range(K):
    A.append(0)
    A = A[1:]
print(*A)
