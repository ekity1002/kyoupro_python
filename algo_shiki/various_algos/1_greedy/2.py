N = int(input())
ans=0
cnt=N
while cnt>0:
    #print(cnt, ans)
    if cnt%2==0:
        cnt = cnt // 2
    else:
        cnt -= 1
    ans+=1
print(ans)