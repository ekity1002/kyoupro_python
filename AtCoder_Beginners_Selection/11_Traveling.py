
def check(cx, cy, t, x, y):
    dx = abs(x - cx)
    dy = abs(y - cy)
    if dx + dy > t:
        return False
    # 残り時間と差分がともに奇数 or 偶数の場合
    if ((dx + dy) & 1) != (t & 1):
        return False
    return True


n = int(input())
ct, cx, cy = 0, 0, 0
for _ in range(n):
    t, x, y = map(int, input().split())
    result = check(cx, cy, t - ct, x, y)
    if not result:
        print('No')
        break
    ct, cx, cy = t, x, y
else:
    print('Yes')