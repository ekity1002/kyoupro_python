N = int(input())
A, B, C = map(int, input().split())
a, b, c = 0, 0, 0

MAX_C = N // C
if MAX_C > 9999:
    MAX_C = 9999

# print(MAX_C)
ans = 10**10
for nc in range(MAX_C, -1, -1):
    MAX_B = (N - C * nc) // B
    if MAX_B > 9999:
        MAX_B = 9999
    for nb in range(MAX_B, -1, -1):
        res = N - C * nc - B * nb  # 残り
        if res % A:
            continue
        na = int(res / A)
        ans = min(ans, na + nb + nc)
print(ans)
