from collections import defaultdict

N = int(input())
users = dict()
ans = []
for i in range(N):
    S = input()
    if users.get(S) is None:
        users[S] = 1
        ans.append(i + 1)

[print(s) for s in ans]
