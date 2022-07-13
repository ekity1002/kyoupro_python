N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

ans = 0
for i,n in enumerate(A):
    if i%2==0:
        ans+=n
    else:
        ans-=n
print(ans)

