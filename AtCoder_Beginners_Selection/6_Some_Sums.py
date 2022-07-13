N,A,B = map(int, input().split())
ans = 0
for i in range(1, N+1, 1):
    s = 0
    for c in str(i):
        s+=int(c)
    if A <= s <= B:
        ans+=i
print(ans)
