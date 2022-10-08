# スイッチクエリ
N, S = map(int, input().split())
Q = int(input())


def switch(x, S):
    # x 番目のスイッチの状態を反転
    S = S ^ (1 << x)
    return S


def check(x, S):
    return S & (1 << x)


for i in range(Q):
    q, x = map(int, input().split())

    if q == 0:
        S = switch(x, S)
    else:
        if check(x, S):
            print("on")
        else:
            print("off")
