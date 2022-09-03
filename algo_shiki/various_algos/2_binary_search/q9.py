N,K = map(int, input().split())

cnt = 0
for i in range(N):
    cnt += min(N, int(K/(i+1)))
print(cnt)