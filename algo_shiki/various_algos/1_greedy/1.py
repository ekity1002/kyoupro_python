N = int(input())

ans = 0
res = N
while True:
    cnt = res // 5
    ans += cnt
    res -= cnt * 5
    #print(cnt, ans, res)
 
    cnt = res // 1
    ans += cnt
    #print(cnt, ans, res)
    break
print(ans)