import sys
input = sys.stdin.readline

N = int(input())
S1, S2 = [0]*N, [0]*N
s1,s2=0,0
#print(S1)

for n in range(N):
    c, p = list(map(int, input().split()))
    if c==1:
        s1+=p
    else:
        s2+=p
    S1[n] = s1
    S2[n] = s2

#print(S1, S2)

Q = int(input())
# L, R = []
for q in range(Q):
    L, R = list(map(int, input().split()))
    if L==R:
        s1, s2 = S1[R-1], S2[R-1]
    elif L == 1:
        s1 = S1[R-1]
        s2 = S2[R-1]
    else:
        s1 = S1[R-1] - S1[L-2]
        s2 = S2[R-1] - S2[L-2]
        
    print(f'{s1} {s2}')
