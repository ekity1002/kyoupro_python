# 領域加算、２次元いもす法
N = int(input())
LX, LY, RX, RY = [], [], [], []
for i in range(N):
    lx, ly, rx, ry = map(int, input().split())
    LX.append(lx)
    LY.append(ly)
    RX.append(rx)
    RY.append(ry)
cnt = [[0] * 1009 for _ in range(1009)]
# print(cnt)

for i in range(N):
    cnt[LX[i]][LY[i]] += 1
    cnt[LX[i]][RY[i]] -= 1
    cnt[RX[i]][LY[i]] -= 1
    cnt[RX[i]][RY[i]] += 1

for i in range(0, 1000):
    for j in range(1, 1000):
        # print(i, j)
        cnt[i][j] += cnt[i][j - 1]

for i in range(1, 1001):
    for j in range(0, 1001):
        cnt[i][j] += cnt[i - 1][j]

answer = [0] * (N + 1)
for i in range(0, 1000):
    for j in range(0, 1000):
        if cnt[i][j] >= 1:
            answer[cnt[i][j]] += 1
# print(cnt)
for i in range(1, N + 1):
    print(answer[i])
