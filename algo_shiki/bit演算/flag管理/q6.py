N = int(input())
result = []
for i in range(len(bin(N))):
    if N & 1 << i:
        result.append(i)
print(len(result))
print(*result)
