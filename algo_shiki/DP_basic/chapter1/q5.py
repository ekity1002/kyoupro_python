# 無限大を表す値 (1000000 にしておく)
INF = 1000000

# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 計算の舞台となる配列を宣言
T = [INF] * N

# 初期値を定める
T[0] = 0

# 順に計算していく
for i in range(1, N):
    for j in range(1, M+1):
        if i-j >= 0:
            T[i] = min(T[i], T[i-j] + A[i] * j)
print(T[-1])