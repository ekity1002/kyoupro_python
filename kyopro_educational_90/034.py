# 034 - There are few types of elements（★4）
from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
d = dict()


ans = 0
cr = 0
cnt = 0
M = defaultdict(int)
# from pdb import set_trace as st

# st()
for i in range(N):
    while cr < N:
        if M[A[cr]] == 0 and cnt == K:
            break
        if M[A[cr]] == 0:
            cnt += 1  # 観ている列に含まれる数の種類
        M[A[cr]] += 1  # A[cr] を参照した数 M[A[0]]  = 1, cr=1,
        cr += 1

    ans = max(ans, cr - i)
    if M[A[i]] == 1:
        cnt -= 1
    M[A[i]] -= 1
# print(d)
# print(M)
print(ans)
