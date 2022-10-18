# A - A Recursive Function

N = int(input())


def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x - 1)


ans = f(N)
print(ans)
