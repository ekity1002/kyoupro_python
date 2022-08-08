N = int(input())

P = [-1]*N
for i in range(N):
    if i==0:
        P[i]=1
    elif i==1:
        P[i]=2
    elif i==2:
        P[i]=4
    else:
        P[i] = P[i-3] + P[i-2] + P[i-1]

print(P[N-1])