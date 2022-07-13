S = input()
T=''
s1='dream'
s2='dreamer'
s3='erase'
s4='eraser'
i=len(S)
while True:
    if i<=0:
        break
    if S[i-5:i]==s1:
        T = s1 + T
        i-=5
    elif S[i-7:i] == s2:
        T = s2 + T
        i-=7
    elif S[i-5:i] == s3:
        T = s3 + T
        i-=5
    elif S[i-6:i] == s4:
        T = s4 + T
        i-=6
    else:
        break
if S==T: print('YES')
else: print('NO')