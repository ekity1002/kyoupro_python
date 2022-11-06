# B - Broken Rounding
from decimal import Decimal, ROUND_HALF_UP

X, K = map(int, input().split())

for i in range(K):
    # i のくらいで四捨五入
    X = int(Decimal(X).quantize(Decimal(f"1E{i+1}"), rounding=ROUND_HALF_UP))

print(X)
