S = input()
ans = 0
for s in S:
    if s == "v":
        ans += 1
    elif s == "w":
        ans += 2
print(ans)
