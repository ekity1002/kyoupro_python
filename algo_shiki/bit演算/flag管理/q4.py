N = int(input())
F = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans += 2 ** F[i]

print(ans)
