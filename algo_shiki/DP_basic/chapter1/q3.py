N = int(input())
S = [-1] * N

for i in range(N):
    if i == 0:
        S[i] = 1
    elif i == 1:
        S[i] = 2
    else:
        S[i] = S[i-1] + S[i-2]
print(S[N-1])
