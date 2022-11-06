import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

ans = []


def calc(E):
    y = -(L / 2) * math.sin(2 * math.pi * E / T)
    z = (L / 2) * (1 - math.cos(2 * math.pi * E / T))
    rad = math.atan2(z, math.sqrt((X**2 + (Y - y) ** 2)))
    return rad * 180 / math.pi


for i in range(Q):
    E = int(input())
    ans.append(calc(E))

[print(a) for a in ans]
