N, X = map(int, input().split())
if N & (1 << X):
    print("Yes")
else:
    print("No")
