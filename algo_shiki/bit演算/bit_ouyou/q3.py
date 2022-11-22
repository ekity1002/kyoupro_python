X = list(map(int, input().split()))
ans = []
for x in X:
    op = 3 << 14
    # print(bin(op))
    cols = []
    for i in range(8):
        # print(x, op, x & op, bin(x & op))
        # print(bin(x), bin(op))
        if x & op == 2 ** (15 - 2 * i):
            # 10: siro
            cols.append("x")
        elif x & op == 2 ** (15 - 2 * i - 1):
            cols.append("o")
        else:
            cols.append(".")
        op = op >> 2
    ans.append(cols)

for col in ans:
    print("".join(col))
