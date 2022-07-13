A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for i in range(A, -1, -1):
    s1 = i*500
    if (s1)>X:
        continue
    if s1==X: 
        ans+=1
        continue
    for j in range(B, -1, -1):
        s2 = j*100
        if (s1+s2)>X: 
            continue
        if (s1+s2)==X: 
            ans+=1
            continue
        for k in range(C, -1, -1):
            s3 = k*50
            if (s1+s2+s3)==X:
                ans += 1
                break
print(ans)