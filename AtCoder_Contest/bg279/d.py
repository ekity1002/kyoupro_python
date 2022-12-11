import math

A, B = map(int, input().split())
l = 0
r = int(A / B)  # 考察より、l,rの間の何処かにある
g = 1


def f(n):
    return B * n + A / math.sqrt(g + n)


# 三分探索
# かいがある範囲が十分に小さくなるまで続ける
while r - l > 2:
    m1 = (l * 2 + r) / 3
    m2 = (l + r * 2) / 3
    if f(m1) > f(m2):
        # 左側が大きいなら、左端を中央に寄せる
        l = int(m1)
    else:
        r = int(m2)

ans = f(0)  # A
# print(l, r)
for i in range(l, r + 1):
    ans = min(ans, f(i))
print(f"{ans:.10f}")
