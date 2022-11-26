# 033 - Not Too Bright（★2）
import math

H, W = map(int, input().split())

if H == 1 or W == 1:
    print(max(H, W))
else:
    print(math.ceil(H / 2) * math.ceil(W / 2))
