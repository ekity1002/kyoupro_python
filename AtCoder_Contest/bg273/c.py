# C - (K+1)-th Largest Number
N = int(input())
A = list(map(int, input().split()))

d = dict()
for i in range(N):
    if d.get(A[i]) is not None:
        d[A[i]] += 1
    else:
        d[A[i]] = 1
    # print(d)

d = dict(sorted(d.items(), key=lambda item: item[0], reverse=True))
# print(d)

for k, v in d.items():
    print(v)

for i in range(N - len(d)):
    print(0)
