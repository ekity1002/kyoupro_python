from collections import defaultdict, deque
from copy import deepcopy

N, M = map(int, input().split())
A = list(map(int, input().split()))
ALL_SUM = sum(A)
D = defaultdict(int)  # カードごとの枚数
for a in A:
    D[a] += 1

D = sorted(list(D.items()))  # (数字、枚数)のリスト（数字が小さい順）
ans = 10**9
sum_tmp = 0
check_idx = 0
i = 0
S = set()

print(D)
from pdb import set_trace as st

st()
if len(D) == 1:
    print(0)
    exit()

while True:
    card, num = D[i]
    sum_tmp += card * num

    if card < M - 1:
        next_card, _ = D[i + 1]
        if card + 1 != next_card:
            # 和を計算
            ans = min(ALL_SUM - sum_tmp, ans)
            sum_tmp = 0
            if i in S:
                break
    elif card == M - 1:
        next_card, _ = D[0]
        if 0 != next_card:
            # 和を計算
            ans = min(ALL_SUM - sum_tmp, ans)
            sum_tmp = 0
            if i in S:
                break

    S.add(i)

    if card == D[-1][0]:
        i = 0
    else:
        i += 1

print(ans)
